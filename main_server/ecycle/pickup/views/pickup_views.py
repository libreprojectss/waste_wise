from django.shortcuts import render
from rest_framework.views import APIView
from pickup.serializers import *
from pickup.models import *
from rest_framework.response import Response
from account.permissions import IsCustomer,IsPicker
from pickup.helpers.pickups_by_location import get_arranged_pickups_by_location
from rest_framework.permissions import IsAuthenticated
from account.models import Notifications
import datetime

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
                Notifications.objects.create(user=request.user,message="Your pickup has been recorded sucessfully. Please  keep track of the pickups from the pickups page")
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


class SetPickupCompleted(APIView):
    permission_classes=[IsAuthenticated,IsPicker]

    def post(self,request):
        pickup_id=request.data.get("pickup_id",None)
        try:
            pickup=pickups.objects.get(id=pickup_id)
        except:
            return Response({"message":"Pickup id is invalid","type":"error"})
        pickup.picked_by=request.user
        pickup.picked_on=datetime.datetime.now()
        pickup.status="completed"
        pickup_requests=picker_pickups.objects.get(picker=request.user)
        pickup_requests.pickups.remove(pickup)
        if(len(pickup_requests.pickups.all())==0):
            pickup_requests.is_free=True
        Notifications.objects.create(user=request.user,message="Hurray! Thank you for completing all the assigned pickups")
        pickup_requests.save()
        pickup.save()
        return Response({"message":"Pickup marked completed sucessfully","type":"success","data":None})
        