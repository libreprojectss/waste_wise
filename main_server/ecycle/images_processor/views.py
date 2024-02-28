from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from images_processor.serializers.image_serializer import ImageSerializer
from images_processor.handler.object_detector import detect_object
# Create your views here.

class Images(APIView):
    def get(self,request):
        return render(request,"index.html")
    def post(self,request):
        print(request.data)
        serializer=ImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            imageObj=serializer.save()
            classifiedResult=detect_object(imageObj)
            return Response({"message":"success","result":classifiedResult})
        else:
            return Response({"message":"error"},status=status.HTTP_400_BAD_REQUEST)
