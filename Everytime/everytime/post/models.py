from django.db import models
from user.models import User
import os
from uuid import uuid4
from django.utils import timezone

def upload_filepath(instance, filename):
    today_str = timezone.now().strftime("%Y%m%d")
    file_basename = os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'

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
    scrap = models.ManyToManyField(to = User, through="Scrap", related_name="scrap_posts")
    image = models.ImageField(upload_to = upload_filepath, blank = True)
    video = models.FileField(upload_to = upload_filepath, blank = True)

    # 제목을 title로 변경하기
    def __str__(self):
        return f'[{self.title}] {self.title}'
    
class Like(models.Model):
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name="post_likes")
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name="user_likes")

class Scrap(models.Model):
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name="post_scrap")
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name="user_scrap")

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