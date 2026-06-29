from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from task_manager.models import Status, Task

class TaskCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.user2 = User.objects.create_user(username='otheruser', password='pass123')
        self.client.login(username='testuser', password='testpass123')
        self.status = Status.objects.create(name='Test Status')
    
    def test_task_create(self):
        response = self.client.post(reverse('task_create'), {
            'name': 'Test Task',
            'status': self.status.pk,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
    
    def test_task_update(self):
        task = Task.objects.create(name='Old Task', status=self.status, author=self.user)
        response = self.client.post(reverse('task_update', args=[task.pk]), {
            'name': 'Updated Task',
            'status': self.status.pk,
        })
        task.refresh_from_db()
        self.assertEqual(task.name, 'Updated Task')
    
    def test_task_delete_by_author(self):
        task = Task.objects.create(name='To Delete', status=self.status, author=self.user)
        response = self.client.post(reverse('task_delete', args=[task.pk]))
        self.assertEqual(Task.objects.count(), 0)
    
    def test_task_delete_by_non_author(self):
        task = Task.objects.create(name='Others Task', status=self.status, author=self.user2)
        response = self.client.post(reverse('task_delete', args=[task.pk]))
        self.assertEqual(Task.objects.count(), 1)
        self.assertRedirects(response, reverse('tasks'))

class StatusCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
    
    def test_status_create(self):
        response = self.client.post(reverse('status_create'), {'name': 'New Status'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Status.objects.count(), 1)
    
    def test_status_update(self):
        status = Status.objects.create(name='Old Status')
        response = self.client.post(reverse('status_update', args=[status.pk]), {'name': 'Updated Status'})
        status.refresh_from_db()
        self.assertEqual(status.name, 'Updated Status')
    
    def test_status_delete(self):
        status = Status.objects.create(name='To Delete')
        response = self.client.post(reverse('status_delete', args=[status.pk]))
        self.assertEqual(Status.objects.count(), 0)

class SimpleTest(TestCase):
    def test_something(self):
        self.assertEqual(1, 1)
from task_manager.models import Label

class LabelCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')
    
    def test_label_create(self):
        response = self.client.post(reverse('label_create'), {'name': 'New Label'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Label.objects.count(), 1)
    
    def test_label_update(self):
        label = Label.objects.create(name='Old Label')
        response = self.client.post(reverse('label_update', args=[label.pk]), {'name': 'Updated Label'})
        label.refresh_from_db()
        self.assertEqual(label.name, 'Updated Label')
    
    def test_label_delete(self):
        label = Label.objects.create(name='To Delete')
        response = self.client.post(reverse('label_delete', args=[label.pk]))
        self.assertEqual(Label.objects.count(), 0)

class TaskFilterTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.user2 = User.objects.create_user(username='otheruser', password='pass123')
        self.client.login(username='testuser', password='testpass123')
        self.status = Status.objects.create(name='Test Status')
        self.task1 = Task.objects.create(name='Task 1', status=self.status, author=self.user)
        self.task2 = Task.objects.create(name='Task 2', status=self.status, author=self.user2)
        self.label = Label.objects.create(name='Test Label')
        self.task1.labels.add(self.label)
    
    def test_filter_only_self(self):
        response = self.client.get('/tasks/', {'only_self': 'on'})
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')
    
    def test_filter_by_status(self):
        response = self.client.get('/tasks/', {'status': self.status.pk})
        self.assertContains(response, 'Task 1')
        self.assertContains(response, 'Task 2')
    
    def test_filter_by_labels(self):
        response = self.client.get('/tasks/', {'labels': self.label.pk})
        self.assertContains(response, 'Task 1')
        self.assertNotContains(response, 'Task 2')
