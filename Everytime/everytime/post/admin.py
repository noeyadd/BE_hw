from django.contrib import admin

# admin 사이트에 모델 등록
from .models import *

admin.site.register(Post)

# 카테고리 admin
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('title',)}

admin.site.register(Category, CategoryAdmin)