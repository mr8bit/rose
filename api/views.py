from django.shortcuts import render
from rest_framework import routers, serializers, viewsets , generics 
from django.shortcuts import render 
from .models import * 
from .serializers import * 
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class PlayListAdvertisingViewSet(viewsets.ModelViewSet):
	serializer_class = PlayListAdvertisingSerializer
	queryset = PlayListAdvertising.objects.all()
	def list(self, request, *args, **kwargs):
		self.object_list = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(self.object_list, many=True)
		return Response({'playlistadvertisings': serializer.data})

class EventViewSet(viewsets.ModelViewSet):
	serializer_class = EventSerializer
	queryset = Event.objects.all()
	def list(self, request, *args, **kwargs):
		self.object_list = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(self.object_list, many=True)
		return Response({'event': serializer.data})

class NewsViewSet(viewsets.ModelViewSet):
	serializer_class = NewsSerializer
	queryset = News.objects.all()
	def list(self, request, *args, **kwargs):
		self.object_list = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(self.object_list, many=True)
		return Response({'news': serializer.data})

class ShopViewSet(viewsets.ModelViewSet):
	serializer_class = ShopSerializer
	queryset = Shop.objects.all()
	def list(self, request, *args, **kwargs):
		self.object_list = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(self.object_list, many=True)
		return Response({'shops': serializer.data})

class TrackViewSet(viewsets.ModelViewSet):
	serializer_class = TrackSerializer
	queryset = Track.objects.all()
	def list(self, request, *args, **kwargs):
		self.object_list = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(self.object_list, many=True)
		return Response({'tracks': serializer.data})