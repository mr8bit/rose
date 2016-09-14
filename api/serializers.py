from rest_framework import serializers
from .models import * 
from django.db import models
class EventSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Event
		fields = ('id', 'name',  'date', 'description' , 'image')

class TrackSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Track
		fields = ('id', 'name',  'status' )

class NewsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = News
		fields = ('id', 'title',  'date', 'description','image')

class  AdvertisingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Advertising
		fields = ('id', 'name',  'type', 'time', 'file')

class  CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'name')

class  ShopSerializer(serializers.ModelSerializer):
	category =   serializers.StringRelatedField(source='category.name', read_only=True, many =False)
	class Meta:
		model = Shop
		fields = ('id', 'name',  'category', 'description', 'image','location')

class PlayListAdvertisingSerializer(serializers.ModelSerializer):
	advertisings = AdvertisingSerializer(many=True,read_only=True)
	class Meta:
		model = PlayListAdvertising
		fields = ('id' , 'name','advertisings')

