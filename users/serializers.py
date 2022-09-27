from rest_framework import serializers
from .models import *


class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        read_only_fields = (
            "is_staff",
            "last_login",
            "is_active",
            "is_superuser",
        )
