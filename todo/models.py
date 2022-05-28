from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    priority = models.CharField(max_length=10, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
