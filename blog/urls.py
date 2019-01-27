from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    AllPostListView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    FilesListView
)
from . import views

urlpatterns = [
    path('', AllPostListView.as_view(), name='blog-home'),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("files/", FilesListView.as_view(), name="blog-files"),

    path("<str:category>/", PostListView.as_view(), name="blog-category"),
    

]
