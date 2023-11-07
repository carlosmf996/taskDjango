from django.conf import settings
from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    completado = models.BooleanField(default=False)
    published_date= models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title