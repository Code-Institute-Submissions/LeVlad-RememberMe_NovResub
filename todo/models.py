from django.db import models

# creating a new model called Item

class Item(models.Model):


    name = models.CharField(max_length=50, null=False, blank=False)
    priority = models.CharField(max_length=10, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

# Overiding the standard return method of the models

    def __str__(self):
        return self.name
