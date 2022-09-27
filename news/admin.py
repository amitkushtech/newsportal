from django.contrib import admin
from .models import NewsCategories, News


# Register your models here.
class NewsCategory(admin.ModelAdmin):
    fields = ("news_category",)


admin.site.register(NewsCategories, NewsCategory)


# class News(admin.ModelAdmin):
#     fields = ("category",)


admin.site.register(News)
