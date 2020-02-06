from django.db import models

# Create your models here.
class Todo(models.Model):
    date_added = models.DateTimeField()
    text = models.CharField(max_length=200)
