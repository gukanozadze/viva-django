from django import forms
from .models import Post
from django.utils import timezone

class PostCreateForm(forms.ModelForm, forms.Form):

    class Meta:
        model = Post
<<<<<<< HEAD
        fields = ('title', 'content', 'category')
=======
        fields = ('content', 'category', 'files')
>>>>>>> 95bae65afa5a38e31e6279dad1c2eb12f3aa0429
