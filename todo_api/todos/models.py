from django.db import models

class Task(models.Model):
    text = models.CharField(max_length=300)
    completed = models.BooleanField()