from .serializers import SignupSerializer,LoginSerializer,AccountSerializer,PickerLocationsSerializer
from rest_framework.views import APIView
from account.renderers import UserRenderer
from rest_framework.response import Response
from account.models import User,Picker_Locations
from account.permissions import IsPicker
from .helpers import get_tokens_for_user
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
#View for signup
class UserCreateView(APIView):
    # renderer_classes=[UserRenderer] #Renderer class to render the response format
    def post(self,request):
        serializeddata=SignupSerializer(data=request.data)
        if serializeddata.is_valid(raise_exception=True):
            data=serializeddata.save()
            user=User.objects.get(email=data.email)
            serialized_user=AccountSerializer(user)
            token=get_tokens_for_user(user)
            return Response({"success":"Account created sucessfully.","token":token,"user":serialized_user.data},status=status.HTTP_200_OK)

class PickerCreateView(APIView):
    def post(self, request):
        print("Request Data:", request.data)
        serializeddata = SignupSerializer(data=request.data)

        if serializeddata.is_valid(raise_exception=True):
            picker = serializeddata.save()

            serialized_user = AccountSerializer(picker)
            token = get_tokens_for_user(picker)

            return Response({"success": "Picker account created successfully.", "token": token, "user": serialized_user.data}, status=status.HTTP_200_OK)


#View for login
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            token = serializer.validated_data['token']
            if serializer.validated_data["is_verified"]:
                user=User.objects.get(email=request.data["email"])
                serialized_data=AccountSerializer(user).data
                

                return Response({'token': token,
                                 'success': "Login successful",
                                  'user':serialized_data},
                                  status=status.HTTP_200_OK)
            else:
                
                return Response({'error':'User is not verified'},status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#View for login
class PickerLoginView(APIView):
    def post(self, request):
       
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            picker=User.objects.filter(email=request.data["email"],is_picker=True)
            if not picker:
                return Response({'error':'No picker account registered with the provided credentials'},status=status.HTTP_404_NOT_FOUND)
            token = serializer.validated_data['token']
            if serializer.validated_data["is_verified"]:
                user=User.objects.get(email=request.data["email"])
                serialized_data=AccountSerializer(user).data
                return Response({'token': token,
                                 'success': "Login successful",
                                  'user':serialized_data},
                                  status=status.HTTP_200_OK)
            else:
                
                return Response({'error':'User is not verified'},status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUserById(APIView):
    def get(self,request,id):
        try:
            user=User.objects.get(id=id)
        except:
            return Response({"message":"Provided id is invalid","type":"error"},400)
        serialized_data=AccountSerializer(user)
        return Response({"message":"Data fetched successfully","type":"success","data":serialized_data.data},200)
        

class NotificationViews(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        notifications=Notifications.objects.filter(user=request.user)
        serialized_data=NotificationSerializer()

class PickerLocationsViews(APIView):
        permission_classes=[IsAuthenticated,IsPicker]
        def post(self,request):
            picker_locations=PickerLocationsSerializer(data=request.data)
            picker_locations.is_valid(raise_exception=True)
            location_objs=Picker_Locations.objects.filter(user=request.user)
            if(len(location_objs)>0):
                location_obj=location_objs[0]
                location_obj.lat=request.data["lat"]
                location_obj.lng=request.data["lng"]
                location_obj.save()
            else:
                picker_locations.save(user=request.user)
            return Response({"message":"Picker locations recorded sucessfully","type":"success","data":None},200)
