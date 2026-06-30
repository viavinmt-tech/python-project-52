from task_manager.tests.base_view_test import BaseViewTestCase

class StatusViewsTest(BaseViewTestCase):
    def test_statuses_list_requires_login(self):
        self.test_list_requires_login('statuses')
    
    def test_statuses_list_with_login(self):
        self.test_list_with_login('statuses')
