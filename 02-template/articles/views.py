import random
from django.shortcuts import render


# Create your views here.
# 1. Variable (변수 전달)
def index(request):
    context = {
        'name' : 'SSAFY',
    }
    return render(request, 'articles/index.html', context)


# 2. Filters
def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    context = {
        'foods':foods, 
        'picked':picked, 
    }
    return render(request, 'articles/dinner.html', context)
 

def search(request):

    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    # print(f'리퀘스트 내용:{request}')  
    # # 리퀘스트 내용:<WSGIRequest: GET '/catch/?message=%EC%98%A4%EC%9E%89'>
    # print(type(request)) 
    # # <class 'django.core.handlers.wsgi.WSGIRequest'>
    # print(request.GET)
    # # <QueryDict: {'message': ['오잉']}> 
    # # 장고 내부의 딕셔너리 타입
    # print(request.GET.get('message'))   # 오잉

    message = request.GET.get('message')
    context = {
        'message':message,
    }
    return render(request, 'articles/catch.html', context)

def detail(request, num):
    context = {
        'num':num, 
    }
    return render(request, 'articles/detail.html', context)
