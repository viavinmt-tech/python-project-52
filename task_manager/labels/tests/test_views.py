from task_manager.tests.base_view_test import BaseViewTestCase

class LabelViewsTest(BaseViewTestCase):
    def test_labels_list_requires_login(self):
        self.test_list_requires_login('labels')
    
    def test_labels_list_with_login(self):
        self.test_list_with_login('labels')
