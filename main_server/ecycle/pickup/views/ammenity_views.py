from django.shortcuts import render
from rest_framework.views import APIView
from pickup.serializers import *
from account.renderers import UserRenderer
from pickup.helpers.amenity import get_amenity
from rest_framework.response import Response 
import urllib.request
import io,json
import zipfile
class GetAmenity(APIView):
    renderer_classes=[UserRenderer]
    def get(self,request):
        res= get_amenity("waste_basket")
        url = res['result']['download_url']
        response = urllib.request.urlopen(url)

        with zipfile.ZipFile(io.BytesIO(response.read()), 'r') as zip_ref:
            with zip_ref.open('Pokhara_buildings.geojson') as file:
                my_export_geojson=json.loads(file.read())
            json_data=my_export_geojson["features"]
            result_list = [{'coordinates': feature['geometry']['coordinates'], 'name': feature['properties']['name']} for feature in json_data]
        return Response(result_list)