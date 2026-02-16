from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<int:pk>/', views.toggle_like, name='toggle_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]