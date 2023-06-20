from django.db import models
from django.utils import timezone
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_finished = models.DateTimeField(default=timezone.now)
    priority = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    

