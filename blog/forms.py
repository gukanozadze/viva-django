from django import forms
from .models import Post
from django.utils import timezone

class PostCreateForm(forms.ModelForm, forms.Form):

    class Meta:
        model = Post
        fields = ('content', 'category', 'files')
