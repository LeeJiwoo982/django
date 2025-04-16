from rest_framework import serializers
from .models import Article

# 게시글 전체 필드를 직렬화
class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = "__all__"

# 게시글 일부 필드 직렬화
class ArticleListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ('id', 'title', 'content',)
