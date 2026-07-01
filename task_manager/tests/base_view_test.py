from django.urls import reverse
from task_manager.tests.base import BaseTestCase

class BaseViewTestCase(BaseTestCase):
    def test_list_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse(self.url_name))
        self.assertEqual(response.status_code, 302)
    
    def test_list_with_login(self):
        response = self.client.get(reverse(self.url_name))
        self.assertEqual(response.status_code, 200)
