from django.test import TestCase
from task_manager.statuses.models import Status

class StatusModelTest(TestCase):
    def test_status_creation(self):
        status = Status.objects.create(name='Test Status')
        self.assertEqual(str(status), 'Test Status')
