from django.urls import reverse
from task_manager.tests.base import BaseTestCase

class BaseViewTestCase(BaseTestCase):
    def test_list_requires_login(self, url_name):
        self.client.logout()
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 302)
    
    def test_list_with_login(self, url_name):
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)
