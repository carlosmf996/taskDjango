from django.conf import settings
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    completado = models.BooleanField(default=False)


    def __str__(self):
        return self.title