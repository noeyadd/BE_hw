from django.db import models
from user.models import User

# 카테고리
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return f'[{self.title}]'

# Post 클래스 정의
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    anonymity = models.BooleanField(default=True)
    author = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "posts")
    category = models.ManyToManyField(to = Category, through="PostCategory", related_name="posts")
    like = models.ManyToManyField(to = User, through="Like", related_name="liked_posts")

    # 제목을 title로 변경하기
    def __str__(self):
        return f'[{self.title}] {self.title}'
    
class Like(models.Model):
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name="post_likes")
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name="user_likes")

# 중간테이블
class PostCategory(models.Model):
    category = models.ForeignKey(to = Category, on_delete=models.CASCADE, related_name="categories_postcategory")
    post = models.ForeignKey(to = Post, on_delete=models.CASCADE, related_name="posts_postcategory")
    
class Comment(models.Model):
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name = "comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "comments")
    anonymity = models.BooleanField(default=True)

    def __str__(self):
        return f'[{self.id}] {self.content}'