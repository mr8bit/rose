from django.contrib import admin
from .models import * 
# Register your models here.

class AdvertisingAdmin(admin.ModelAdmin): # Модель админа 
     list_display = ('name', 'type')
admin.site.register(Advertising, AdvertisingAdmin)


class TrackAdmin(admin.ModelAdmin): # Модель админа 
     list_display = ('name','status')
admin.site.register(Track, TrackAdmin)

class CategoryAdmin(admin.ModelAdmin): # Модель админа 
     list_display = ('name',)
admin.site.register(Category, CategoryAdmin)

class ShopAdmin(admin.ModelAdmin): # Модель админа 
     list_display = ('name',)
admin.site.register(Shop, ShopAdmin)


class PlayListAdvertisingAdmin(admin.ModelAdmin): # Модель админа 
     list_display = ('name',)
admin.site.register( PlayListAdvertising, PlayListAdvertisingAdmin)