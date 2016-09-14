"""rose URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import *
urlpatterns = [
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'playlistadvertising', PlayListAdvertisingViewSet)
router.register(r'event', EventViewSet)
router.register(r'track', TrackViewSet)
router.register(r'shops', TrackViewSet)


router.register(r'news', NewsViewSet)


urlpatterns += router.urls