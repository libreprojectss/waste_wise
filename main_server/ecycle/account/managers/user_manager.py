from django.db import models
class CustomerManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(is_picker=False)
class PickerManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return super().get_queryset(*args,**kwargs).filter(is_picker=True)