from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from django.conf import settings

class Post(models.Model):
    CATEGORY_CHOICES = (('all', 'all'),
                        ('drone', 'Drone'),
                        ('management', 'Management'),
                        ('SOS', 'SOS'))


    content = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    files = models.FileField(upload_to='documents', null=True, blank=True)

    author =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

   
    def __str__(self):
        return self.content[:10]

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

