from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from django.contrib.auth.decorators import login_required

def list(request):
    categories = Category.objects.all()
    posts = Post.objects.all().order_by('-id')[:4] # Post 객체를 내림차순으로 모두 불러온 후 posts 변수에 담음
    return render(request, 'post/list.html', {'posts' : posts, 'categories' : categories})

#CRUD - Create
@login_required # 로그아웃 상태로 글 작성 버튼을 누르면 로그인 페이지로 연결됨
def create(request, slug):
    categories = Category.objects.all()

    if request.method == "POST":
        category = Category.objects.get(slug=slug)

        title = request.POST.get('title')
        content = request.POST.get('content')
        anonymity = 'anonymity' in request.POST     # True, False 체크하기

        video = request.FILES.get('video')
        image = request.FILES.get('image')

        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id = category_id) for category_id in category_ids]

        # post 객체
        post = Post.objects.create(
            title = title,
            content = content,
            anonymity = anonymity,
            author = request.user,
            image = image,
            video = video,
        )

        post.category.add(category)

        # 다대다 카테고리 연결
        # for category in category_list:
            # post.category.add(category)

        return redirect('post:category', slug)                 # id 정도만 같이 보낼 수 있음 ('list', id)
    return render(request, 'post/list.html', {'categories' : categories})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category).order_by('-id')

    return render(request, 'post/category.html', {'posts' : posts, 'category' : category})

# CRUD - Read
def detail(request, id):
    post = get_object_or_404(Post, id = id)     # 객체가 있으면 post 반환, 없으면 404 에러
    return render(request, 'post/detail.html', {'post' : post})

# CRUD - Update
def update(request, id):
    post = get_object_or_404(Post, id = id)     # 객체가 있으면 post 반환, 없으면 404 에러
    if request.method == "POST":                # 만약 POST일 때만 수정
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.anonymity = 'anonymity' in request.POST
        video = request.FILES.get('video')
        image = request.FILES.get('image')

        if video:
            post.video.delete()
            post.video = video
        if image:
            post.image.delete()
            post.image = image

        post.save()                             # update에서는 save() 필수
        return redirect('post:detail', id)           # 수정 후에는 detail.html로 redirect 된다
    return render(request, 'post/update.html', {'post' : post})

# CRUD - Delete
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('post:list')

# 블로그 댓글
def create_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.method == "POST":
        Comment.objects.create(
            content = request.POST.get('content'),
            author = request.user,
            post = post,
            anonymity = 'anonymity' in request.POST
        )
        return redirect('post:detail', post_id)
    
# 댓글 삭제
def delete_comment(request, post_id):
    comment = get_object_or_404(Comment, id = post_id)
    post_id = comment.post.id  # 댓글이 달린 포스트의 ID를 저장
    comment.delete()
    return redirect('post:detail', post_id)
    
# 좋아요 누르기
def add_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like.add(request.user)
    return redirect('post:detail', post_id)

# 좋아요 취소
def remove_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like.remove(request.user)
    return redirect('post:detail', post_id)

# 스크랩 하기
def add_scrap(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.scrap.add(request.user)
    return redirect('post:detail', post_id)

# 스크랩 취소
def remove_scrap(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.scrap.remove(request.user)
    return redirect('post:detail', post_id)
