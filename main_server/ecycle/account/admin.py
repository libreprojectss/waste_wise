# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import User, Customer, Picker, Notifications, Picker_Locations


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'user_id',
        'email',
        'name',
        'phone_number',
        'account_created',
        'is_picker',
        'is_admin',
        'is_staff',
        'is_email_verified',
        'is_verified',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'account_created',
        'is_picker',
        'is_admin',
        'is_staff',
        'is_email_verified',
        'is_verified',
    )
    raw_id_fields = ('groups', 'user_permissions')
    search_fields = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'user_id',
        'email',
        'name',
        'phone_number',
        'account_created',
        'is_picker',
        'is_admin',
        'is_staff',
        'is_email_verified',
        'is_verified',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'account_created',
        'is_picker',
        'is_admin',
        'is_staff',
        'is_email_verified',
        'is_verified',
    )
    search_fields = ('name',)


@admin.register(Picker)
class PickerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'user_id',
        'email',
        'name',
        'phone_number',
        'account_created',
        'is_picker',
        'is_admin',
        'is_staff',
        'is_email_verified',
        'is_verified',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'account_created',
        'is_picker',
        'is_admin',
        'is_staff',
        'is_email_verified',
        'is_verified',
    )
    search_fields = ('name',)


@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message')
    list_filter = ('user',)


@admin.register(Picker_Locations)
class Picker_LocationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'lat', 'lng')
    list_filter = ('user',)
