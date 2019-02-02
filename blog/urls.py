from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    PostListView,
    PostDetailView,
    AllPostListView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    FilesListView,
    UserFilesListView,
    CreatePost
)
from . import views

urlpatterns = [
    path('', AllPostListView.as_view(), name='blog-home'),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", CreatePost, name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("files/", FilesListView, name="blog-files"),
    path("files/<int:username>", UserFilesListView, name="user-files"),
    
    path("post/<str:category>/", PostListView.as_view(), name="blog-category"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)