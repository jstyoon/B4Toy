from rest_framework import serializers

from .models import ArticleTodolist

class ArticleSerializer(serializers.ModelSerializer):
    verified_user = serializers.SerializerMethodField()
    def get_verified_user(self,obj):
        return obj.verified_user.name
    
    class Meta:
        model = ArticleTodolist
        fields = ('title', 'verified_user')


class ArticleTodolistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTodolist
        fields = ("title", "is_complete", "content")


class ArticleTodolistSerializer(serializers.ModelSerializer):
    verified_user = serializers.SerializerMethodField()
    
    def get_verified_user(self, obj):
        return obj.verified_user.email
    
    class Meta:
        model = ArticleTodolist
        fields = "__all__"
