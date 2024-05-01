from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/list.html', {'posts':posts})

def search(request):
    data = request.GET['searchtext']
    # 쿼리셋 사용 (contains과 Q)
    posts = Post.objects.filter(title__contains = data) | Post.objects.filter(content__contains = data)
    return render(request, 'posts/search.html', {'posts':posts, 'data':data})

# CRUD - Create
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        post = Post.objects.create(
            title = title,
            content = content,
        )
        return redirect('list')
    return render(request, 'posts/create.html')

# CRUD - Read
def detail(request, id):
    post = get_object_or_404(Post, id = id)
    # 조회수 증가
    post.views += 1
    post.save()
    
    return render(request, 'posts/detail.html', {'post' : post})

# CRUD - Update
def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('detail', id)
    return render(request, 'posts/update.html', {'post' : post})

# CRUD - Delete
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('list')