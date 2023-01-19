from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.items, name='item'),
]
