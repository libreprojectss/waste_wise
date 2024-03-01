import grpc_files.cluster.cluster_pb2 as cluster__pb2
import grpc_files.cluster.cluster_pb2_grpc as cluster__pb2_grpc
import grpc

from django.shortcuts import render
from rest_framework.views import APIView
from pickup.serializers import *
from rest_framework.response import Response
from django.core.files.base import ContentFile
import json
import base64
from pickup.helpers.pickups_by_location import get_arranged_pickups_by_location
from rest_framework.permissions import IsAuthenticated

coordinates=[
     { "lat": 37.826, "lng": -122.422 },
     { "lat": -29.145, "lng": 153.456 },
     { "lat": 45.678, "lng": -75.890 },
     { "lat": -12.345, "lng": 67.890 },
     { "lat": 55.432, "lng": 12.345 },
     { "lat": -8.901, "lng": 145.678 },
     { "lat": 33.456, "lng": -118.901 },
     { "lat": -41.234, "lng": 174.567 },
     { "lat": 20.567, "lng": 78.901 },
     { "lat": -3.456, "lng": 102.345 },
     { "lat": 61.789, "lng": -149.567 },
     { "lat": -23.456, "lng": 47.890 },
     { "lat": 38.901, "lng": -77.234 },
     { "lat": -14.567, "lng": 167.890 },
     { "lat": 53.234, "lng": 9.012 },
     { "lat": -17.890, "lng": 31.234 },
     { "lat": 48.901, "lng": -66.789 },
     { "lat": -9.012, "lng": 140.567 },
     { "lat": 35.678, "lng": -80.123 },
     { "lat": -25.678, "lng": 132.345 }
 ]


def get_priority_queue():
    channel = grpc.insecure_channel('localhost:50051')  
    stub = cluster__pb2_grpc.ClusterServiceStub(channel)
    request = cluster__pb2.Coordinates()
    print("request",request)
    for coord in coordinates:
        coordinate = request.coordinate.add()
        coordinate.lat = coord['lat']
        coordinate.lng = coord['lng']
    response = stub.GeneratePriorityQueue(request)
    return response.cluster

class ClusterPickupView(APIView):
    def get(self,request):
        data=get_priority_queue()
        print(data)
        response_dict = {
        'clusters': [
            {
                'centroid': {
                    'location_name':cluster.centroid.location_name,
                    'lat': cluster.centroid.lat,
                    'lng': cluster.centroid.lng
                },
                'points': [point for point in cluster.points],
                'max_radius': cluster.max_radius,
                'density_ratio': cluster.density_ratio
            }
            for cluster in data
        ]
    }        
        return Response({"message":"Data fetched sucessfully","type":"success","data":response_dict})

