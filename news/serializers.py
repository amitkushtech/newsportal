from dataclasses import field, fields
from pyexpat import model
from xmlrpc.client import Server
from black import nullcontext
from rest_framework import serializers
from .models import *


class CommentSerializers(serializers.ModelSerializer):
    # reply_count = serializers.SerializerMethodField()
    # parent_id = serializers.PrimaryKeyRelatedField()
    # user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"
        # fields = ("user", "news", "commment", "reply_count")
        def get_fields(self):
            fields = super(CommentSerializers, self).get_fields()
            fields["subcomments"] = CommentSerializers(many=True, read_only=True)
            return fields

        def get_related_field(self, model_field):
            return CommentSerializers()


class RatingSerializer(serializers.ModelSerializer):
    # rating = serializers.StringRelatedField(many=True)

    class Meta:
        model = Rating
        fields = "__all__"


# def get_reply_count(self, obj):
#     if obj.is_parent:
#         return obj.children().count()
#     return 0

# def get_user(self, obj):
#     return obj.user.username


class NewsCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsCategories
        fields = "__all__"


class NewsSerializers(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    # comments = CommentSerializers()
    # tag = serializers.StringRelatedField(many=True, read_only=True)
    comments = CommentSerializers(many=True, read_only=True)
    rating = RatingSerializer(many=True)

    class Meta:
        model = News
        fields = "__all__"
        News.objects.order_by("-added_at")
        # fields = ("user", "title", "image", "detail", "category", "comments")

    # def get_reply_count(self, obj):
    #     if obj.is_parent:
    #         return obj.children().count()
    #     return 0

    # def get_user(self, obj):
    #     return obj.user.username
