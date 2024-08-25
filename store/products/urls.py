from urllib import request
from django.urls import path, include
from .views import getData

urlpatterns = [
    path('test', getData)
]