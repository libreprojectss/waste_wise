from .serializers import SignupSerializer,LoginSerializer,AccountSerializer
from rest_framework.views import APIView
from account.renderers import UserRenderer
from rest_framework.response import Response
from account.models import User
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
            token=get_tokens_for_user(User.objects.get(email=data.email))
            return Response({"success":"Account created sucessfully.","token":token},status=status.HTTP_200_OK)


#View for login
class LoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            token = serializer.validated_data['token']
            if serializer.validated_data["is_verified"]:
                user=AccountSerializer(serializer.validated_data["user"]).data
                

                return Response({'token': token,
                                 'success': "Login successful",
                                  'user':user},
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
