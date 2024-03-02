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
     { "lat": 37.826, "lng": -122.422,"pickup_identifier":1 },
     { "lat": -29.145, "lng": 153.456,"pickup_identifier":2 },
     { "lat": 45.678, "lng": -75.890,"pickup_identifier":3 },
     { "lat": -12.345, "lng": 67.890,"pickup_identifier":4 },
     { "lat": 55.432, "lng": 12.345,"pickup_identifier":5 },
     { "lat": -8.901, "lng": 145.678,"pickup_identifier":6 },
     { "lat": 33.456, "lng": -118.901,"pickup_identifier":7 },
     { "lat": -41.234, "lng": 174.567,"pickup_identifier":8 },
     { "lat": 20.567, "lng": 78.901,"pickup_identifier":9 },
     { "lat": -3.456, "lng": 102.345,"pickup_identifier":10 },
     { "lat": 61.789, "lng": -149.567,"pickup_identifier":11 },
     { "lat": -23.456, "lng": 47.890,"pickup_identifier":12 },
     { "lat": 38.901, "lng": -77.234,"pickup_identifier":13 },
     { "lat": -14.567, "lng": 167.890,"pickup_identifier":14 },
     { "lat": 53.234, "lng": 9.012,"pickup_identifier":15 },
     { "lat": -17.890, "lng": 31.234,"pickup_identifier":16 },
     { "lat": 48.901, "lng": -66.789,"pickup_identifier":17 },
     { "lat": -9.012, "lng": 140.567,"pickup_identifier":18 },
     { "lat": 35.678, "lng": -80.123,"pickup_identifier":19 },
     { "lat": -25.678, "lng": 132.345,"pickup_identifier":20 }
 ]



def get_priority_queue():
    channel = grpc.insecure_channel('localhost:50051')  
    stub = cluster__pb2_grpc.ClusterServiceStub(channel)
    request = cluster__pb2.Coordinates()
    for coord in coordinates:
        coordinate = request.coordinate.add()
        coordinate.lat = coord['lat']
        coordinate.lng = coord['lng']
        coordinate.pickup_identifier=coord["pickup_identifier"]
    response = stub.GeneratePriorityQueue(request)
    return response.cluster

class ClusterPickupView(APIView):
    def get(self,request):
        data=get_priority_queue()
        for cluster in data:
            objects = [json.loads(item) for item in cluster.points]
            print(objects)
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

