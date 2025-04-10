from django.contrib import admin
from .models import Article
# 현재 폴더 안에 있는 models모듈에서 Article 클래스 가져오겠다 명시

# Register your models here.
admin.site.register(Article)    # 게시글 db