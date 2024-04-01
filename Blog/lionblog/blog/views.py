from django.shortcuts import render
from .models import Post

def list(request):
    posts = Post.objects.all().order_by('-id') # Post 객체를 내림차순으로 모두 불러온 후 posts 변수에 담음
    return render(request, 'blog.html', {'posts' : posts})