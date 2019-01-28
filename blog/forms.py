from django import forms
from .models import Post
from django.utils import timezone

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content', 'category']