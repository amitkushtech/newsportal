from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.
class NewsCategoryViewset(viewsets.ModelViewSet):
    queryset = NewsCategories.objects.all()
    serializer_class = NewsCategorySerializers


class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
