from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("newscategory", views.NewsCategoryViewset)
router.register("news", views.NewsViewset)

app_name = "news"
urlpatterns = [
    path("", include(router.urls)),
]
