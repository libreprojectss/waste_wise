from django.db import models

# Create your models here.

class Images(models.Model):
    image=models.ImageField(upload_to="images")
    uploaded_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

class resultImage(models.Model):
    image=models.ImageField(upload_to="resultImages")
    result_of=models.ForeignKey(Images,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)