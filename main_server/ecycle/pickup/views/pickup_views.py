from django.shortcuts import render
from rest_framework.views import APIView
from pickup.serializers import *
from rest_framework.response import Response
from django.core.files.base import ContentFile
import base64
from pickup.helpers.pickups_by_location import get_arranged_pickups_by_location
from rest_framework.permissions import IsAuthenticated

class PickupView(APIView):
    def get(self,request,pickup_id=None):
        data=get_arranged_pickups_by_location()
        print(data)
        return Response({"message":"Data fetched sucessfully","type":"success","data":data})
    
class CreatePickupView(APIView):
        permission_classes=[IsAuthenticated]
        def post(self,request):
            if not request.data.get("products",""):
                return Response({"message":"Products field is required","type":"error"},400)
            serialized_data=PickupSerializer(data=request.data)
            if serialized_data.is_valid(raise_exception=True):
                pickup=serialized_data.save()
            serialized_data=ProductSerializer(data=request.data["products"],many=True)
            if serialized_data.is_valid(raise_exception=True):
                serialized_data.save(user=request.user,pickup=pickup)
            
                return Response({"message":"Pickup request recorded sucessfully","type":"success"},status=status.HTTP_201_CREATED)

class PickedViews(APIView):
    def get(self,request):
        objects=pickups.objects.exclude(picked_on=None)
        data=PickupSerializer(objects,many=True).data
        return Response({"message":"Data fetched sucessfully","type":"success","data":data})
    
class UserPickups(APIView):
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        product_list=products.objects.filter(user=request.user)
        pickups_obj_list=list()
        for i in product_list:
            if i.pickup not in pickups_obj_list:
                pickups_obj_list.append(i.pickup)
        if len(pickups_obj_list)>0:
            serialized_data=PickupSerializer(pickups_obj_list,many=True).data
        else:
            serialized_data=[""]
        return Response({"message":"Data fetched sucessfully","type":"success","data":serialized_data})

