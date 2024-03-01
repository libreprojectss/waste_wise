from rest_framework import permissions
from .models import Customer,Picker

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return not user.is_picker

class IsPicker(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_picker