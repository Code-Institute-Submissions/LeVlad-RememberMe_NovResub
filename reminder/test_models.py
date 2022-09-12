from django.test import TestCase
from .models import Task


class TestModels(TestCase):

    # test to check if the done attribute defaults to False

    def test_done_defaults_to_false(self):
        task = Task.objects.create(name='Test Reminder Task')
        self.assertFalse(task.done)
