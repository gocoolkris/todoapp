from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Todo(models.Model):
	task_name = models.CharField(max_length=200)
	task_status = models.BooleanField(default=False)

