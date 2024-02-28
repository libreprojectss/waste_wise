from django.db import models
from account.models import User

def product_image_upload_to(instance, filename):
    print(instance)
    id_var= instance.id
    # Append the filename to the product id and return the complete path
    return f"/media/{id_var}/product_image/{filename}"

class pickups(models.Model):
    lat=models.FloatField() # For lattitude
    long=models.FloatField() # For longitude
    picked_on=models.DateTimeField(default=None,blank=True,null=True)

    @property
    def is_picked(self):
        if self.picked_on:
            return True
        return False

class products(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pickup=models.ForeignKey(pickups,on_delete=models.CASCADE, related_name="products",default=None,null=True)
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to=product_image_upload_to,default=None,blank=True,null=True)
    description=models.CharField(max_length=255)
    usable=models.BooleanField()




class donate(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    donated_on=models.DateTimeField()
    verified_status=models.BooleanField() # true for verified and false for not verified
    




