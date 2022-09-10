from django.db import models


class Item(models.Model):

    """Creating a new class for items that can inherit from Django
    and use attributes as descriptive options for ToDo list
    """

    name = models.CharField(max_length=50, null=False, blank=False)
    priority = models.CharField(max_length=10, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    """
    Function to override the build-in function to render strings in HTML
    instead of seeing a standard numbering like item1, item 2, the user now
    can see the name of the task
    """

    def __str__(self):
        return str(self.name)
