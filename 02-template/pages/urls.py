from django.urls import path

from . import views
# 현재 위치를 명시하기를 원함
 
app_name = 'pages'
urlpatterns = [
    path('', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('<int:num>/', views.detail),
]
