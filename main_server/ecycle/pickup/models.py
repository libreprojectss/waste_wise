from django.db import models
from account.models import User,Picker
from django.utils.deconstruct import deconstructible
from datetime import datetime

@deconstructible
class ProductImageFilename:
    def __init__(self, subfolder="product_image"):
        self.subfolder = subfolder

    def __call__(self, instance, filename):
        # Generate a unique filename based on the instance's pickup ID
        pickup_id = instance.pickup_id if instance.pickup_id else "no_pickup"
        return f"{self.subfolder}/{pickup_id}/{filename}"

product_image_upload_to = ProductImageFilename()



class pickups(models.Model):
    class ProductStatus(models.TextChoices):
        PENDING = 'pending', 'Pending'
        SCHEDULED = 'scheduled', 'Scheduled'
        COMPLETED = 'completed', 'Completed'
    lat=models.FloatField() 
    lng=models.FloatField() 
    requested_on=models.DateTimeField(auto_now_add=True)
    picked_on=models.DateTimeField(default=None,blank=True,null=True)
    picked_by=models.ForeignKey(Picker,on_delete=models.CASCADE,null=True,blank=True,default=None)
    status = models.CharField(
        max_length=20,
        choices=ProductStatus.choices,
        default=ProductStatus.PENDING,
    )
    
    @property
    def is_picked(self):
        if self.picked_on:
            return True
        return False

    @property
    def is_scheduled(self):
        if self.status=="scheduled":
            return True
        return False
    
    def __str__(self):
        return f"{self.lat},{self.lng}"
    
    def get_products(self):
        return self.products.all()
    
    class Meta:
        ordering=["-picked_on"]

class product(models.Model):
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
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    donated_on=models.DateTimeField()
    verified_status=models.BooleanField()
    
class picker_pickups(models.Model):
    picker = models.OneToOneField(User, on_delete=models.CASCADE)
    pickups = models.ManyToManyField(pickups,blank=True)  
    is_free = models.BooleanField(default=True) 
    
    @classmethod
    def get_free_pickers(cls):
        return cls.objects.filter(is_free=True)


