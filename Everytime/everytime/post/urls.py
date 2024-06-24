from django.urls import path
from .views import *

app_name = 'post'   #네임스페이스

urlpatterns = [
    path('', list, name = "list"),
    path('create/<slug:slug>/', create, name = "create"),
    path('category/<slug:slug>/', category, name = "category"),
    path('detail/<int:id>/', detail, name = "detail"),
    path('update/<int:id>/', update, name = "update"),
    path('delete/<int:id>/', delete, name = "delete"),
    path('create-comment/<int:post_id>/', create_comment, name = "create-comment"),
    path('delete-comment/<int:post_id>/', delete_comment, name = "delete-comment"),
    path('add-like/<int:post_id>/', add_like, name = "add-like"),
    path('remove-like/<int:post_id>/', remove_like, name = "remove-like"),
    path('add-scrap/<int:post_id>/', add_scrap, name = "add-scrap"),
    path('remove-scrap/<int:post_id>/', remove_scrap, name = "remove-scrap"),
]