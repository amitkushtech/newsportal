from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *


class NewsCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsCategories
        fields = "__all__"


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
