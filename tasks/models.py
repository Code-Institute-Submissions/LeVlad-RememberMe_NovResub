from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    """Creating a new class for tasks that can inherit from Django
    and use attributes as descriptive options for Task list
    """
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    priority = models.CharField(max_length=10, null=False, blank=False)
    location = models.CharField(max_length=200, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta Class to order tasks by completion"""
        ordering = ['done']

    def __str__(self):
        return str(self.user)

