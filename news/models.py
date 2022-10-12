from distutils.command.upload import upload
from operator import mod
from re import T
from statistics import mode
from turtle import title
from unicodedata import category
from django.db import models
from users.models import CustomUser
from django.utils import timezone

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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(NewsCategories, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    detail = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
        get_latest_by = "added_at"


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="comments")
    commment = models.TextField()
    commment_date = models.DateField(default=timezone.now)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Commented by {self.user.email} on {self.news}"

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ("-commment_date",)

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True


class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    news = models.ForeignKey(News, related_name="rating", on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ["news"]

    def __str__(self):
        return self.rate
