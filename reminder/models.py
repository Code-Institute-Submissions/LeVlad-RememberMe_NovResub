from django.db import models


class Task(models.Model):

    """Creating a new class for tasks that can inherit from Django
    and use attributes as descriptive options for Task list
    """

    name = models.CharField(max_length=50, null=False, blank=False)
    priority = models.CharField(max_length=10, null=False, blank=False)
    location = models.CharField(max_length=200, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
    created = models.DateTimeField(auto_now_add=True)

    """
    Function to override the build-in function to render strings in HTML
    instead of seeing a standard numbering like item1, item 2, the user now
    can see the name of the task
    """

    def __str__(self):
        return f'There is {self.name} to do in {self.location} \
            with a {self.priority} priority'
