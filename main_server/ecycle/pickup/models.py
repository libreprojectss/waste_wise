from django.db import models
from account.models import User,Picker

def product_image_upload_to(instance, filename):
    id_var= instance.id
    return f"/media/{id_var}/product_image/{filename}"

class pickups(models.Model):
    lat=models.FloatField() 
    long=models.FloatField() 
    picked_on=models.DateTimeField(default=None,blank=True,null=True)
    picked_by=models.ForeignKey(Picker,on_delete=models.CASCADE)

    @property
    def is_picked(self):
        if self.picked_on:
            return True
        return False
    def __str__(self):
        return f"{self.lat},{self.long}"
    
    def get_products(self):
        return self.products.all()
    
    class Meta:
        ordering=["-picked_on"]

class products(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pickup=models.ForeignKey(pickups,on_delete=models.CASCADE, related_name="products",default=None,null=True)
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to=product_image_upload_to,default=None,blank=True,null=True)
    description=models.CharField(max_length=255)
    usable=models.BooleanField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=["-id"]
    
    def get_pickup(self):
        return self.pickup




class donate(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    donated_on=models.DateTimeField()
    verified_status=models.BooleanField()
    




