
from pickup.models import *
from pickup.serializers import ProductSerializer

def get_arranged_pickups_by_location():
    location_dict=dict()
    all_pickups=pickups.objects.all()
    product_list=list()
    for i in all_pickups:
        all_products=products.objects.filter(pickup=i)
        location_str=str(i.lat)+str(i.long)
        if location_str in location_dict.keys():
            for i in all_products:
                location_dict[location_str]["products"].append(ProductSerializer(i).data)
        else:
            location_dict.update({location_str:{"lat":i.lat,"long":i.long,"products":ProductSerializer(all_products,many=True).data}})
    
    return location_dict.values()





