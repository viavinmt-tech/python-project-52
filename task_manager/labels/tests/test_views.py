from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LabelViewsTest(TestCase):
    def test_labels_list_requires_login(self):
        response = self.client.get(reverse('labels'))
        self.assertEqual(response.status_code, 302)
    
    def test_labels_list_with_login(self):
        User.objects.create_user(username='testuser', password='testpass123')  # nosonar
        self.client.login(username='testuser', password='testpass123')  # nosonar
        response = self.client.get(reverse('labels'))
        self.assertEqual(response.status_code, 200)
