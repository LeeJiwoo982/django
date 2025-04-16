from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

# Create your views here.

# 그냥 보내면 500에러
# DRF는 데코레이터 !!필수!!
@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시글 데이터 조회
    if request.method == "GET":
        # DB에서 조회
        articles = Article.objects.all()

        # 인스턴스는 장고에서만 쓸 수 있는 쿼리셋 데이터 타입
        # 시리얼라이저로 변환 진행
        serializer = ArticleListSerializer(articles, many=True) # 여러개 있는 데이터면 many=True로 변경

        # DRF에서 제공하는 Response 사용해 JSON데이터 응답
        # 그냥 던지면 덩어리임
        #  JSON데이터는 serializer의 data속성에 존재
        return Response(serializer.data)
        # 생성, 수정일은 .py에서 걸러서 없음
    
    # 게시글 생성 요청에 대한 응답
    elif request.method == "POST":
        # 예전코드: form = ArticleForm(request.POST)
        # 사용자 입력 데이터를 클래스로 받아서 변환
        serializer = ArticleSerializer(data=request.data)
        # 유효성 검사
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # 단일 게시글 데이터 조회
    article = Article.objects.get(pk=article_pk)   
    if request.method == "GET":
        # 직렬화
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        # 사용자가 보낸 수정 데이터 변환
        serializer = ArticleSerializer(
            article, 
            data=request.data, 
            partial=True
            )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST) is_valid()에 인자를 넣으면 400 생략 가능
