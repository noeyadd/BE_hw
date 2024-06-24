from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from django.contrib.auth.decorators import login_required

def list(request):
    # 존재하는 모든 카테고리 확인할 수 있도록
    categories = Category.objects.all()

    # 선택한 카테고리 id
    category_id = request.GET.get('category')

    # 카테고리 필터링
    if category_id:
        category = get_object_or_404(Category, id = category_id)
        posts = category.posts.all().order_by('-id')
    else :
        posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/blog.html', {'posts' : posts, 'categories' : categories})

#CRUD - Create
@login_required # 로그아웃 상태로 글 작성 버튼을 누르면 로그인 페이지로 연결됨
def create(request):
    categories = Category.objects.all()

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        video = request.FILES.get('video')
        image = request.FILES.get('image')

        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id = category_id) for category_id in category_ids]

        # post 객체
        post = Post.objects.create(
            title = title,
            content = content,
            author = request.user,
            image = image,
            video = video,
        )

        for category in category_list:
            post.category.add(category)

        return redirect('blog:list')                 # id 정도만 같이 보낼 수 있음 ('list', id)
    return render(request, 'blog/create.html', {'categories' : categories})

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
        video = request.FILES.get('video')
        image = request.FILES.get('image')

        if video:
            post.video.delete()
            post.video = video
        if image:
            post.image.delete()
            post.image = image
            
        post.save()                             # update에서는 save() 필수
        return redirect('blog:detail', id)           # 수정 후에는 detail.html로 redirect 된다
    return render(request, 'blog/update.html', {'post' : post})

# CRUD - Delete
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('blog:list')

# 블로그 댓글 연결
def create_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.method == "POST":
        Comment.objects.create(
            content = request.POST.get('content'),
            author = request.user,
            post = post
        )
        return redirect('blog:detail', post_id)
    
# 좋아요
def add_like(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.like.add(request.user)
    return redirect('blog:detail', post_id)

# 좋아요 취소
def remove_like(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.like.remove(request.user)
    return redirect('blog:detail', post_id)

def mylike(request):
    liked_posts = Post.objects.filter(like=request.user).order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts':liked_posts})