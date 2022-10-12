from django.contrib import admin
from .models import NewsCategories, News, Comment, Rating


# Register your models here.
class NewsCategory(admin.ModelAdmin):
    fields = ("news_category",)


admin.site.register(NewsCategories, NewsCategory)


# class News(admin.ModelAdmin):
#     fields = ("category",)


admin.site.register(News)
admin.site.register(Comment)


class Ratings(admin.ModelAdmin):
    fields = (
        "user",
        "news",
        "one",
        "two",
        "three",
        "four",
        "five",
    )


admin.site.register(Rating, Ratings)
