from django.test import TestCase
from task_manager.labels.models import Label

class LabelModelTest(TestCase):
    def test_label_creation(self):
        label = Label.objects.create(name='Test Label')
        self.assertEqual(str(label), 'Test Label')
    
    def test_label_str_method(self):
        label = Label.objects.create(name='Another Label')
        self.assertEqual(str(label), 'Another Label')
