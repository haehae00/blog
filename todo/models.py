from django.db import models
from django. contrib.auth.models import User

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.CharField(max_length=300, blank=True, null=True)
    is_complete = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField( blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title