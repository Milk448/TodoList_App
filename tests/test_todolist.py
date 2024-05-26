import unittest #I have implemented unit test for each python file enenthough we are not obliged to do it I tested all of them as additional since its recommended 
from src.todolist import ToDoList
from src.task import Task

class TestToDoList(unittest.TestCase):
    def test_add_to_do(self):
        to_do_list = ToDoList()
        task = Task("Test", "This is a test task.")
        to_do_list.add_to_do(task)
        self.assertEqual(to_do_list.head.task, task)

    def test_mark_to_do_as_completed(self):
        to_do_list = ToDoList()
        task = Task("Test", "This is a test task.")
        to_do_list.add_to_do(task)
        self.assertTrue(to_do_list.mark_to_do_as_completed("Test"))
        self.assertTrue(task.is_completed())

    def test_view_to_do_list(self):
        to_do_list = ToDoList()
        task1 = Task("Test1", "This is test task 1.")
        task2 = Task("Test2", "This is test task 2.")
        to_do_list.add_to_do(task1)
        to_do_list.add_to_do(task2)
        to_do_list.view_to_do_list()

if __name__ == '__main__':
    unittest.main()
