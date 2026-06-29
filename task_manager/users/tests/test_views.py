from django.test import TestCase
from django.urls import reverse

class UserViewsTest(TestCase):
    def test_users_list_view(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
