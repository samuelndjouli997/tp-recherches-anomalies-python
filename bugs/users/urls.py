from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('user/post/', views.users, name='user')
]
