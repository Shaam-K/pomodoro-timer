from datetime import datetime
from django.db import models
from  django.utils import timezone
# Create your models here.

class tasks_snippet(models.Model):
    task_details = models.CharField(max_length = 100, unique=True)
    due_date = models.DateTimeField()
    task_created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.task_details