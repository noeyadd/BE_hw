from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from post.models import *

# 회원가입 - Form 활용
def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form' : form})
    
    # 사용자가 POST 요청으로 회원가입 폼을 제출했을 때
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('accounts:login')
    else :
        return render(request, 'accounts/signup.html', {'form' : form})
    

# 로그인
def login_view(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html', {'form' : AuthenticationForm})
    
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        login(request, form.user_cache)
        return redirect('post:list')
    return render(request, 'accounts/login.html', {'form' : form})


# 로그아웃
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('post:list')

# 마이페이지
def mypage(request):
    return render(request, 'accounts/mypage.html')

# 내가 작성한 글 확인
def mypost(request):
    posts = request.user.posts.all().order_by('-id')
    return render(request, 'accounts/mypost.html', {'posts' : posts})

def myscrap(request):
    #posts = request.user.posts.all().order_by('-id')
    #scrap_posts = posts.post_scrap.all().order_by('-id')
    # scrap_posts = request.user.user_scrap.all()
    scrap_posts = Post.objects.filter(scrap = request.user).order_by('-id')
    return render(request, 'accounts/myscrap.html', {'scrap_posts' : scrap_posts })