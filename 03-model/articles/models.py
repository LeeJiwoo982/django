from django.db import models

# Create your models here.

# 모델에서 DB 테이블 만들기 실습
# 게시글이 저장될 테이블 설계하는 클래스
# 컬럼이름 등을 설정
class Article(models.Model):    # 파스칼케이스로 이름짓기
    title = models.CharField(max_length=10)                 # 게시글 제목
    content = models.TextField()                            # 게시글 내용
    created_at = models.DateTimeField(auto_now_add=True)    # 생성일
    updated_at = models.DateTimeField(auto_now=True)        # 수정일