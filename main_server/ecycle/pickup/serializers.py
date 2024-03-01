from .models import *
from rest_framework import serializers,status
from django.core.files.base import ContentFile
import base64,os
from django.conf import settings

class ProductSerializer(serializers.ModelSerializer):
    image=serializers.CharField()
    class Meta:
        model=product
        fields="__all__"
        read_only_fields=["user"]
    
    def create(self, validated_data):
        # Extract the base64 content from the received data
        image_data = validated_data.pop('image', None)

        if image_data:
            padding = '=' * (4 - (len(image_data) % 4))
            image_data += padding
            # Decode the base64 string and create a ContentFile
            print(validated_data)
            decoded_image = ContentFile(base64.b64decode(image_data.encode()), name=f'${validated_data["pickup"].id}.png')

           
            validated_data["image"]=decoded_image

        return super().create(validated_data)
    
class PickupSerializer(serializers.ModelSerializer):
    product=ProductSerializer(many=True,read_only=True)
    class Meta:
        model=pickups
        fields=['product','lat','lng','picked_on','is_picked']

    
    