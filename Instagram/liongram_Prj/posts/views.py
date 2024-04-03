from django.shortcuts import render
from .models import Post

def list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'list.html', {'posts':posts})

def search(request):
    data = request.GET['searchtext']

    # 쿼리셋 사용 (contains과 Q)
    posts = Post.objects.filter(title__contains = data) | Post.objects.filter(content__contains = data)

    return render(request, 'search.html', {'posts':posts, 'data':data})