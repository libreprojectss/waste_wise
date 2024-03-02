from pickup.models import picker_pickups,pickups
from account.models import Picker_Locations,User
from geopy.distance import geodesic

picker_locations=[{
    "user":1,
    "lat":20,
    "lng":40
},
{
    "user":2,
    "lat":30,
    "lng":50
},
{
    "user":3,
    "lat":40,
    "lng":60
},

]

# "clusters": [
#             {
#                 "centroid": {
#                     "location_name": "Chipledhunga",
#                     "lat": 28.22463035583496,
#                     "lng": 83.989501953125
#                 },
#                 "points": [
#                     "{\"lat\":-12.345000267028809,\"lng\":67.88999938964844}",
#                     "{\"lat\":20.566999435424805,\"lng\":78.9010009765625}",
#                     "{\"lat\":-23.45599937438965,\"lng\":47.88999938964844}",
#                     "{\"lat\":-17.889999389648438,\"lng\":31.233999252319336}"
#                 ],
#                 "max_radius": 70.73493194580078,
#                 "density_ratio": 2.5447330474853516
#             },
#             {
#                 "centroid": {
#                     "location_name": "Test",
#                     "lat": 27.70328712463379,
#                     "lng": 85.31433868408203
#                 },
#                 "points": [
#                     "{\"lat\":-29.145000457763672,\"lng\":153.45599365234375}",
#                     "{\"lat\":-8.901000022888184,\"lng\":145.67799377441406}",
#                     "{\"lat\":-41.23400115966797,\"lng\":174.56700134277344}",
#                     "{\"lat\":-3.4560000896453857,\"lng\":102.34500122070312}",
#                     "{\"lat\":-14.567000389099121,\"lng\":167.88999938964844}",
#                     "{\"lat\":-9.01200008392334,\"lng\":140.56700134277344}",
#                     "{\"lat\":-25.67799949645996,\"lng\":132.34500122070312}"
#                 ],
#                 "max_radius": 114.19268798828125,
#                 "density_ratio": 1.7087225914001465
#             },
#             {
#                 "centroid": {
#                     "location_name": "Lamachaur",
#                     "lat": 28.282615661621094,
#                     "lng": 83.97223663330078
#                 },
#                 "points": [
#                     "{\"lat\":37.82600021362305,\"lng\":-122.4219970703125}",
#                     "{\"lat\":45.678001403808594,\"lng\":-75.88999938964844}",
#                     "{\"lat\":55.43199920654297,\"lng\":12.345000267028809}",
#                     "{\"lat\":33.45600128173828,\"lng\":-118.9010009765625}",
#                     "{\"lat\":61.78900146484375,\"lng\":-149.56700134277344}",
#                     "{\"lat\":38.9010009765625,\"lng\":-77.23400115966797}",
#                     "{\"lat\":53.23400115966797,\"lng\":9.01200008392334}",
#                     "{\"lat\":48.9010009765625,\"lng\":-66.78900146484375}",
#                     "{\"lat\":35.678001403808594,\"lng\":-80.12300109863281}"
#                 ],
#                 "max_radius": 237.34169006347656,
#                 "density_ratio": 0.5085627436637878
#             },
#             {
#                 "centroid": {
#                     "location_name": "Nadipur",
#                     "lat": 28.233089447021484,
#                     "lng": 83.99046325683594
#                 },
#                 "points": [],
#                 "max_radius": 0.0,
#                 "density_ratio": 0.0
#             }
#         ]

def assign_picker(pickup_points_list):
    pickers=User.objects.filter(is_picker=True)
    for picker in pickers:
        if len(picker_pickups.objects.filter(picker=picker))==0:
            picker_pickups.objects.create(picker=picker)

    load_pickers = picker_pickups.get_free_pickers()
    if(len(load_pickers)==0):
        return None
    #     pickers=Picker.objects.all()
    #     for picker in pickers:
    #         picker_pickups.objects.create(picker=picker)
    #     load_pickers = picker_pickups.get_free_pickers()

    pickers_availability = [{"picker": picker_pickup.picker, "available": True} for picker_pickup in load_pickers]
    if len(pickers_availability)==0:
        print("No picker found")
        return None
    for points in pickup_points_list:
        available_pickers = []
        for picker in pickers_availability:
            if picker["available"]:
                available_pickers.append(picker["picker"])
        print(available_pickers)
        if(len(available_pickers)==0):
            for picker_availability in pickers_availability:
                picker_availability["available"]=True
            for picker in pickers_availability:
                if picker["available"]:
                    available_pickers.append(picker["picker"])
        
        if available_pickers:
            nearest_picker_info = available_pickers[0]
            nearest_distance = float('inf')  

            for picker_info in available_pickers:
                picker_location=Picker_Locations.objects.filter(user=picker_info)[0]
                if not picker_location:
                    continue
                picker_location = (picker_location.lat,picker_location.lng)
                pickup_location=(points["centroid"].lat,points["centroid"].lng)
                distance = geodesic(picker_location, pickup_location).kilometers

                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_picker_info = picker_info
            for point in points["points"]:
                pickup = pickups.objects.get(id=point["pickup_identifier"])
                assigned_picker = nearest_picker_info
                picker_pickup_instance, created = picker_pickups.objects.get_or_create(picker=assigned_picker)
                picker_pickup_instance.pickups.add(pickup)
            for picker in pickers_availability:
                if picker["picker"]==nearest_picker_info:
                    picker["available"]=False
            picker=picker_pickups.objects.get(picker=nearest_picker_info)
            if len(picker.pickups.all())!=0:
                picker.is_free=False
            else:
                picker.is_free=True
            picker.save()
        else:
            print("No available pickers for point", point["pickup_identifier"])


    

