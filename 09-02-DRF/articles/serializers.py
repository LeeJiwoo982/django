from rest_framework import serializers 
from .models import Article, Comment


# 게시글의 일부 필드를 직렬화 하는 클래스
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


# 게시글의 전체 필드를 직렬화 하는 클래스
class ArticleSerializer(serializers.ModelSerializer):
    
    # comment_set에 활용할 댓글 데이터 가공하는 도구
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content', )
    
    # 기존에 있던 역참조 매니저인 comment_set의 값을 덮어쓰기
    # 게시글 입장에서 댓글은 1:N
    # 매니트루해야 댓글 없어도 괜찮
    comment_set = CommentDetailSerializer(read_only=True, many=True)

    # 새로운 필드 생성
    num_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    # 값을 채울 함수
    def get_num_of_comments(self, obj):
        # 여기서 obj는 특정 게시글 인스턴스임
        # obj.comment_set.count()s
        
        # view함수에서 annotate 해서 생긴 새로운 속성 결과를 사용할 수 있게 됨
        # 같은 이름을 쓰는거는 약속!!
        return obj.num_of_comments


# 댓글의 전체 필드를 직렬화하는 클래스
class CommentSerializer(serializers.ModelSerializer):
    
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title', )
    
    # 외래 키 필드인 아티클의 데이터 재구성
    article = ArticleTitleSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        # # 읽기 전용 필드 설정
        # read_only_fields = ('article', )