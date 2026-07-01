from django.urls import reverse
from task_manager.tests.base import BaseTestCase

class BaseViewTestCase(BaseTestCase):
    url_name = None
    
    def test_list_requires_login(self):
        if self.url_name is None:
            return
        self.client.logout()
        response = self.client.get(reverse(self.url_name))
        self.assertEqual(response.status_code, 302)
    
    def test_list_with_login(self):
        if self.url_name is None:
            return
        response = self.client.get(reverse(self.url_name))
        self.assertEqual(response.status_code, 200)
