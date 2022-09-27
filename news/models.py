from distutils.command.upload import upload
from operator import mod
from statistics import mode
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.
class NewsCategories(models.Model):
    # TYPE = (
    #     ("Sports", "Sports"),
    #     ("Politics", "Politics"),
    #     ("Science and Technology", "Science and Technology"),
    #     ("History", "History"),
    #     ("Others", "Others"),
    # )
    news_category = models.CharField(max_length=40)

    def __str__(self):
        return self.news_category

    class Meta:
        verbose_name_plural = "News categories"


class News(models.Model):
    category = models.ForeignKey(NewsCategories, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    detail = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
