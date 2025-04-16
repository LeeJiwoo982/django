from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.


# @api_view(['GET'])
@api_view()
def article_json(request):  #인자
    articles = Article.objects.all()    #게시글 조회
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
    # form, 렌더 ,리다이렉트 없음
    # 데이터를 가공 해서 응답
    # 전체 데이터를 json으로 준거임
