from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('mood-stats/', views.mood_stats, name='mood_stats'),
    path('like/<int:pk>/', views.toggle_like, name='toggle_like'),
    path(
        'comment/<int:pk>/edit/',
        views.CommentUpdateView.as_view(),
        name='comment_edit',
    ),
    path(
        'comment/<int:pk>/delete/',
        views.CommentDeleteView.as_view(),
        name='comment_delete',
    ),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
