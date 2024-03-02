from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import User
from account.serializers import AccountSerializer,SignupSerializer
from pickup.models import product
from pickup.serializers import ProductSerializer

# Create your views here.
class Pickers(APIView):
    def get(self,request):
        all_pickers=User.objects.all()
        serialized_data=AccountSerializer(all_pickers,many=True)
        return Response({"message":"Pickers fetched sucessfully","type":"success","data":serialized_data.data},200)
    
    def post(self, request):
        serializeddata = SignupSerializer(data=request.data)

        if serializeddata.is_valid(raise_exception=True):
            picker = serializeddata.save(is_picker=True)
            serialized_user = AccountSerializer(picker)
            return Response({"message": "Picker account created successfully.","user": serialized_user.data},200)

    def delete(self,request,user_id):
        try:
            user=User.objects.get(user=user_id)
        except:
            return Response({"message": "Picker with the provided id doesn't exists."},400)

        user.delete()
        return Response({"message": "Picker deleted sucessfully."},200)

class Products(APIView):
    def get(self,request):
        products=product.objects.all()
        product_data=ProductSerializer(products,many=True)
        return Response({"message":"Products fetched sucessfully","type":"success","data":product_data.data},status=status.HTTP_200_OK)

