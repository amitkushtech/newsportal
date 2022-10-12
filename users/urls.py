from tkinter import N
from django.urls import path, include, re_path
from allauth.account.views import confirm_email

# from django.urls import re_path as url
from django.contrib import admin
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("users", views.CustomUserViews)

app_name = "users"
urlpatterns = [
    path("", include(router.urls)),
    path("login", views.LoginAPIView().as_view(), name="login"),
    path("logout", views.LogoutView().as_view(), name="logout"),
    path("change-password", views.ChangePasswordView().as_view(), name="changepassword")
    # path("rest-auth/", include("rest_auth.urls")),
    # path("rest-auth/registration/", include("rest_auth.registration.urls")),
    # path("account/", include("allauth.urls")),
    # path(
    #     "accounts-rest/registration/account-confirm-email/(?P<key>.+)/$",
    #     confirm_email,
    #     name="account_confirm_email",
    # ),
]
