from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

# models.py에 Post 클래스 정의하기
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "posts")
    category = models.ManyToManyField(to = Category, through = "PostCategory", related_name = "posts")
    like = models.ManyToManyField(to = User, through="Like", related_name="liked_posts")
    

    # 제목을 title로 변경하기
    def __str__(self):
        return self.title

# 중간테이블(Post - User)
class Like(models.Model):
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name = "post_likes")
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "user_likes")
    
class Comment(models.Model):
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name="commnets")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "comments")

    def __str__(self):
        return f'[{self.id}] {self.content}'
    
    
class PostCategory(models.Model):
    category = models.ForeignKey(to = Category, on_delete = models.CASCADE, related_name="categories_postcategory")
    post = models.ForeignKey(to = Post, on_delete = models.CASCADE, related_name="posts_postcategory")
    
