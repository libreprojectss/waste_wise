# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import pickups, product, donate, picker_pickups


@admin.register(pickups)
class pickupsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'lat',
        'lng',
        'requested_on',
        'picked_on',
        'picked_by',
        'status',
    )
    list_filter = ('requested_on', 'picked_on', 'picked_by')


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'pickup',
        'title',
        'image',
        'description',
        'usable',
    )
    list_filter = ('user', 'pickup', 'usable')


@admin.register(donate)
class donateAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'donated_on', 'verified_status')
    list_filter = ('product', 'donated_on', 'verified_status')


@admin.register(picker_pickups)
class picker_pickupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'picker', 'is_free')
    list_filter = ('picker', 'is_free')
    raw_id_fields = ('pickups',)
