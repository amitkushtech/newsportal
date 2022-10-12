from cProfile import label
from re import U
from tkinter.ttk import Style
from urllib import request
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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

    def validate(self, data):
        emails = data.get("email")
        if CustomUser.objects.filter(email=emails).exists():
            print("Already Exist")
            raise serializers.ValidationError(
                "Sorry!! the email address already exist."
            )
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email")
    password = serializers.CharField(
        label="Password", style={"input_type": "password"}, write_only=True
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                email=email,
                password=password,
            )
            if not user:
                return Response(
                    {"message": "Email or password didnt match."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                return Response(
                    {"message": " Both Email and password are required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        attrs["user"] = user
        return user


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ["password", "is_staff", "is_superuser"]


class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
