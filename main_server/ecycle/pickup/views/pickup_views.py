from django.shortcuts import render
from rest_framework.views import APIView
from pickup.serializers import *
from pickup.models import *
from rest_framework.response import Response
from django.core.files.base import ContentFile
import base64
from account.permissions import IsCustomer,IsPicker
from pickup.helpers.pickups_by_location import get_arranged_pickups_by_location
from rest_framework.permissions import IsAuthenticated

class PickupView(APIView):
    def get(self,request,pickup_id=None):
        data=get_arranged_pickups_by_location()
        return Response({"message":"Data fetched sucessfully","type":"success","data":data})
    
class CreatePickupView(APIView):
        permission_classes=[IsAuthenticated,IsCustomer]
        def post(self,request):
            if not request.data.get("product",""):
                return Response({"message":"Product field is required","type":"error"},400)
            serialized_data=PickupSerializer(data=request.data)
            if serialized_data.is_valid(raise_exception=True):
                pickup=serialized_data.save()
            product_serialize=ProductSerializer(data=request.data["product"])
            if product_serialize.is_valid(raise_exception=True):
                product_serialize.save(user=request.user,pickup=pickup)
            
                return Response({"message":"Pickup request recorded sucessfully","type":"success"},status=status.HTTP_201_CREATED)





class PickedViews(APIView):
    def get(self,request):
        objects=pickups.objects.filter(status="completed").exclude(picked_on=None)
        data=PickupSerializer(objects,many=True).data
        return Response({"message":"Data fetched sucessfully","type":"success","data":data})
    
class UserPickups(APIView):
    permission_classes=[IsAuthenticated,IsCustomer]
    
    def get(self,request):
        product_list=product.objects.filter(user=request.user)
        pickups_obj_list=list()
        for i in product_list:
            if i.pickup not in pickups_obj_list:
                pickups_obj_list.append(i.pickup)
        if len(pickups_obj_list)>0:
            serialized_data=PickupSerializer(pickups_obj_list,many=True).data
        else:
            serialized_data=[""]
        return Response({"message":"Data fetched sucessfully","type":"success","data":serialized_data})

class PickerPickups(APIView):
    permission_classes=[IsAuthenticated,IsPicker]
    
    def get(self,request):
        try:
            picker_pickups_instance = picker_pickups.objects.get(picker=request.user)
        except:
            return Response({"message":"No any pickups available for now","type":"success","data":[]})

        pickups_queryset = picker_pickups_instance.pickups.all()
        print(pickups_queryset)

        if len(pickups_queryset)!=0:
            serialized_data=PickupSerializer(pickups_queryset,many=True).data
        else:
            serialized_data=[]
        return Response({"message":"Data fetched sucessfully","type":"success","data":serialized_data})
