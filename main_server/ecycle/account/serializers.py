from .models import User,Notifications
from django.contrib.auth import authenticate
from rest_framework import serializers,status
from phonenumber_field.phonenumber import to_python
from .helpers import get_tokens_for_user
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import check_password
from phonenumber_field.serializerfields import PhoneNumberField

class SignupSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, max_length=200)
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = ('password', 'email', 'phone_number', 'name', 'confirm_password','is_picker')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return password


    def validate_phone_number(self, value):
        #Checks if the phone number is unique
        if User.objects.filter(phone_number=value).exists():
                raise serializers.ValidationError("This phone number is already in use.")
        phone_number = to_python(value)
        if phone_number:
            #Check if the phone number starts with +27
            if str(phone_number.country_code) != '977':
                raise serializers.ValidationError("Only Nepal based phone numbers are allowed.")
            return value
        else:
            raise serializers.ValidationError("Phone number is not valid")

    def validate(self, data):
        password_confirm = data.pop('confirm_password')
        if data["password"] != password_confirm:
            raise serializers.ValidationError("The passwords don't match")
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True,max_length=200)
    password=serializers.CharField(required=True,max_length=200)
    class Meta:
        fields=['email','password']
    
    def validate(self,data):
        if not User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError("No any user is registered with this email")
        user=User.objects.get(email=data["email"])
        if user.check_password(data["password"]):
            token=get_tokens_for_user(user)
            return {'token':token,'is_verified': True,"user":user}
        else:
            raise serializers.ValidationError('Invalid credentials')
        return data
    
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude=["password","groups","user_permissions"]

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notifications
        fields="__all__"
        read_only_fields=["user"]