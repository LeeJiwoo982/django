from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        # 그냥 Form은 첫 인자로 request를 받아야 함
        # 두 번째가 Data : request.POST
        if form.is_valid():
            auth_login(request, form.get_user())
            # 로그인 인증된 유저 객체를 뽑아야 함
            # form 인스턴스에 있음. '.get_user()'
            # auth_login : 인증된 사용자의 세션을 생성헤줌.
            # 유효성 검사를 통과할 경우 로그인 한 사용자 객체를 반환
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')