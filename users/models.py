from operator import mod
from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractBaseUser):
    ROLE = (
        ("READ", "READER"),
        ("WRITE", "WRITER"),
    )
    username = None
    email = models.EmailField(_("email address"), unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=ROLE, blank=True, null=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
