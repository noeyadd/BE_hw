from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def list(request):
    posts = Post.objects.all().order_by('-id') # Post 객체를 내림차순으로 모두 불러온 후 posts 변수에 담음
    return render(request, 'blog/blog.html', {'posts' : posts})

#CRUD - Create
def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        # post 객체
        post = Post.objects.create(
            title = title,
            content = content,
        )

        return redirect('list')                 # id 정도만 같이 보낼 수 있음 ('list', id)
    return render(request, 'blog/create.html')

# CRUD - Read
def detail(request, id):
    post = get_object_or_404(Post, id = id)     # 객체가 있으면 post 반환, 없으면 404 에러
    return render(request, 'blog/detail.html', {'post' : post})

# CRUD - Update
def update(request, id):
    post = get_object_or_404(Post, id = id)     # 객체가 있으면 post 반환, 없으면 404 에러
    if request.method == "POST":                # 만약 POST일 때만 수정
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()                             # update에서는 save() 필수
        return redirect('detail', id)           # 수정 후에는 detail.html로 redirect 된다
    return render(request, 'blog/update.html', {'post' : post})

# CRUD - Delete
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('list')