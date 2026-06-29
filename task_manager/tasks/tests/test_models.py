from django.test import TestCase
from django.contrib.auth.models import User
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

class TaskModelTest(TestCase):
    def test_task_creation(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        status = Status.objects.create(name='Test Status')
        task = Task.objects.create(
            name='Test Task',
            description='Test Description',
            status=status,
            author=user
        )
        self.assertEqual(str(task), 'Test Task')
