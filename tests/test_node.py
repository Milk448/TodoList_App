import unittest
from src.node import Node
from src.task import Task

def test_node_creation():
    task = Task("Test", "This is a test task.")
    node = Node(task)
    assert node.task == task
    assert node.next is None
#   I have implemented unit test for each python file enenthough we are not obliged to do it I tested all of them as additional since its recommended 