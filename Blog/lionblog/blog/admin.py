from django.contrib import admin

# admin 사이트에 모델 등록
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Category)






