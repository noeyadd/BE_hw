from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('signup/', signup_view, name = "signup"),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('my-page/', mypage, name = "my-page"),
    path('my-post/', mypost, name = "my-post"),
]