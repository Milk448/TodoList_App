import unittest
from src.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test", "This is a test task.")
        self.assertEqual(task.get_title(), "Test")
        self.assertEqual(task.get_description(), "This is a test task.")
        self.assertFalse(task.is_completed())

    def test_mark_completed(self):
        task = Task("Test", "This is a test task.")
        task.mark_completed()
        self.assertTrue(task.is_completed())

if __name__ == '__main__':
    unittest.main()
