from django.db import models

MAX_CHARS = 300

class Project(models.Model):
    name = models.CharField(max_length=MAX_CHARS)

class Task(models.Model):
    text = models.CharField(max_length=MAX_CHARS)
    completed = models.BooleanField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)