from task_manager.tests.base_view_test import BaseViewTestCase

class TaskViewsTest(BaseViewTestCase):
    def test_tasks_list_requires_login(self):
        self.test_list_requires_login('tasks')
    
    def test_tasks_list_with_login(self):
        self.test_list_with_login('tasks')
