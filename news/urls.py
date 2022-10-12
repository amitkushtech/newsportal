from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("newscategory", views.NewsCategoryViewset)
router.register("news", views.NewsViewset)
router.register("comments", views.CommentViewset)
router.register("rating", views.RatingViewset)

app_name = "news"
urlpatterns = [
    path("", include(router.urls)),
]
