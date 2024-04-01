from django.db import models

# models.py에 Post 클래스 정의하기
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # 제목을 title로 변경하기
    def __str__(self):
        return self.title