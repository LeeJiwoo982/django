from django.contrib import admin
# 명시적 상대경로
from .models import Article


# Register your models here.
# 어드민 사이트에 등록한다.(모델클래스를)
admin.site.register(Article)
