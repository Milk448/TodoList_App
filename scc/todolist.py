from node import Node

class ToDoList:
    def __init__(self):
        self.head = None

    def add_to_do(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def mark_to_do_as_completed(self, title):
        current = self.head
        while current:
            if current.task.get_title() == title:
                current.task.mark_completed()
                return True
            current = current.next
        return False

    def view_to_do_list(self):
        current = self.head
        if not current:
            print("The to-do list is empty.")
        else:
            while current:
                task = current.task
                status = "Completed" if task.is_completed() else "Not Completed"
                print(f"Title: {task.get_title()}, Description: {task.get_description()}, Status: {status}")
                current = current.next
