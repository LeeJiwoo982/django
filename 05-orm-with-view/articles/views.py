from django.shortcuts import render, redirect
from .models import Article


# 메인 페이지를 응답하는 함수 (+ 전체 게시글 목록)
def index(request):
    # DB에 전체 게시글 요청 후 가져오기
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 특정 단일 게시글의 상세 페이지를 응답
# + 단일 게시글 조회
def detail(request, pk):
    # pk로 들어온 정수 값을 활용해 DB id가 pk인 게시글 조회 요청
    article = Article.objects.get(pk=pk)
    # print(article)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)

# 게시글을 작성하기 위한 페이지(form)을 제공하는 함수
def new(request):
    return render(request, 'articles/new.html')

# 사용자에게 데이터를 받아 저장하고 페이지를 응답(제공)하는 함수(할일이 많다)
def create(request):
    # 사용자에게 받은 데이터를 추출해야 함
    # request 안에 사용자 입력 데이터 있음
    # print(request.GET)
    # <QueryDict: {'title': ['싸피'], 'content': ['파이썬']}>
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 저장 요청
    # 1. 인스턴스 생성 후 
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()  # 제일 중요

    # # 2. 인스턴스 생성하면서 변수 입력 후 save()
    article = Article(title=title, content=content)
    # 유효성 검사를 하기 위해서는 2번을 추천!
    article.save()

    # # 3. 바로 쿼리셋을 사용해서 생성. save 필요 없음
    # Article.objects.create(title=title, content=content)
    
    # 포스트는 데이터 조작이라 페이지를 응답할 필요가 없다.
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    # 어떤 게시글을 지우는지 먼저 조회
    article = Article.objects.get(pk=pk)
    # DB에 삭제 요청
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    
    return redirect('articles:detail', article.pk)