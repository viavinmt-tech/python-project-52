from django.test import TestCase
from django.urls import reverse

class StatusViewsTest(TestCase):
    def test_statuses_list_view_requires_login(self):
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 302)
