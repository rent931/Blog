from django.urls import path
from .views import (
    PostCreateView,
    PostDeleteView,
    PostListView, 
    PostDetailedView, 
    PostUpdateView
)

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('posts/<int:pk>/', PostDetailedView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    
]