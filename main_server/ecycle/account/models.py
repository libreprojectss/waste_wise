from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from account.managers.user_manager import CustomerManager,PickerManager
import uuid
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    user_id=models.UUIDField(default=uuid.uuid4)
    email = models.EmailField(unique=True)
    name=models.CharField(max_length=255)
    phone_number =PhoneNumberField(unique=True)
    account_created=models.DateField(auto_now_add=True,blank=True)
    is_picker=models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False,null=False)
    is_verified = models.BooleanField(default=False,null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin



class Customer(User):
    objects = CustomerManager()
    class Meta:
        proxy = True

    def __str__(self):
        return f"Customer: {self.email}"


class Picker(User):
    objects = PickerManager()
    class Meta:
        proxy = True

    def __str__(self):
        return f"Picker: {self.email}"


class Notifications(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    message=models.CharField( max_length=50)
