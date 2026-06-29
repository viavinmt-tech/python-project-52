from django.test import TestCase
from task_manager.labels.models import Label

class LabelModelTest(TestCase):
    def test_label_creation(self):
        label = Label.objects.create(name='Test Label')
        self.assertEqual(str(label), 'Test Label')
