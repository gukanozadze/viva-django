from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms


class Post(models.Model):
    CATEGORY_CHOICES = (
        ('all', 'all'),
        ('drone', 'drone'),
        ('management', 'management'),
        ('sos', 'sos')

    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(default='all', max_length=100, choices = CATEGORY_CHOICES)
    file_field = models.FileField(null=True)
    
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

