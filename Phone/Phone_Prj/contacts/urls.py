from django.urls import path
from .views import list, search, create, detail, update, delete

urlpatterns = [
    path('', list, name="list"),
    path('result/', search, name="search"),
    path('create/', create, name="create"),
    path('detail/<int:id>/', detail, name = "detail"),
    path('update/<int:id>/', update, name = "update"),
    path('delete/<int:id>/', delete, name = "delete"),
]