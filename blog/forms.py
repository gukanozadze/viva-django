from django import forms
from .models import Post
from django.utils import timezone


class PostCreateForm(forms.Form):
    CATEGORY_CHOICES = (('all', 'all'),
                        ('drone', 'Drone'),
                        ('management', 'Management'),
                        ('SOS', 'SOS'))


    title = forms.CharField()
    content = forms.CharField()
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    files = forms.FileField()
    #(widget=forms.ClearableFileInput(attrs={'multiple': True})
