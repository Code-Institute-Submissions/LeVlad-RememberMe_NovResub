from django.test import TestCase
from tasks.models import Task


class TestViews(TestCase):

    def test_can_get_reminer_list_html(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('reminder/reminder_list.html')

    def test_add_task_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('reminder/add_task.html')

    def test_edit_task_page(self):
        task = Task.objects.create(name='Test Reminder Task')
        response = self.client.get(f'/edit/{task.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('reminder/edit_task.html')

    def test_add_task(self):
        response = self.client.post('/add', {'name': 'Test Added Task'})
        self.assertRedirects(response, '/')

    def test_delete_task(self):
        task = Task.objects.create(name='Test Reminder Task')
        response = self.client.get(f'/delete/{task.id}')
        self.assertRedirects(response, '/')
        existing_tasks = Task.objects.filter(id=task.id)
        self.assertEqual(len(existing_tasks), 0)

    def test_can_change_task(self):
        task = Task.objects.create(name='Test Reminder Task', done=True)
        response = self.client.get(f'/toggle/{task.id}')
        self.assertRedirects(response, '/')
        updated_task = Task.objects.get(id=task.id)
        self.assertFalse(updated_task.done)

    def test_can_edit_task(self):
        task = Task.objects.create(name='Test Reminder Task')
        response = self.client.post(f'/edit/{task.id}',{'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.name, 'Updated Name')
