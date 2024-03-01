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
     { "lat": 37.826, "long": -122.422 },
     { "lat": -29.145, "long": 153.456 },
     { "lat": 45.678, "long": -75.890 },
     { "lat": -12.345, "long": 67.890 },
     { "lat": 55.432, "long": 12.345 },
     { "lat": -8.901, "long": 145.678 },
     { "lat": 33.456, "long": -118.901 },
     { "lat": -41.234, "long": 174.567 },
     { "lat": 20.567, "long": 78.901 },
     { "lat": -3.456, "long": 102.345 },
     { "lat": 61.789, "long": -149.567 },
     { "lat": -23.456, "long": 47.890 },
     { "lat": 38.901, "long": -77.234 },
     { "lat": -14.567, "long": 167.890 },
     { "lat": 53.234, "long": 9.012 },
     { "lat": -17.890, "long": 31.234 },
     { "lat": 48.901, "long": -66.789 },
     { "lat": -9.012, "long": 140.567 },
     { "lat": 35.678, "long": -80.123 },
     { "lat": -25.678, "long": 132.345 }
 ]


def get_priority_queue():
    channel = grpc.insecure_channel('localhost:50051')  
    stub = cluster__pb2_grpc.ClusterServiceStub(channel)
    request = cluster__pb2.Coordinates()
    print("request",request)
    for coord in coordinates:
        coordinate = request.coordinate.add()
        coordinate.lat = coord['lat']
        coordinate.long = coord['long']
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
                    'long': cluster.centroid.long
                },
                'points': [point for point in cluster.points],
                'max_radius': cluster.max_radius,
                'density_ratio': cluster.density_ratio
            }
            for cluster in data
        ]
    }        
        return Response({"message":"Data fetched sucessfully","type":"success","data":response_dict})

