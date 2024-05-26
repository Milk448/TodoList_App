from task import Task
from todolist import ToDoList

def main():
    to_do_list = ToDoList()

    to_do_list.add_to_do(Task("Buy groceries", "Milk, Eggs, Bread, Butter"))
    to_do_list.add_to_do(Task("Read book", "Read 'The Pragmatic Programmer'"))
    to_do_list.add_to_do(Task("Workout", "30 minutes of cardio"))

    print("To-Do List:")
    to_do_list.view_to_do_list()
    print("\n")

    to_do_list.mark_to_do_as_completed("Read book")

    print("Updated To-Do List:")
    to_do_list.view_to_do_list()

if __name__ == "__main__":
    main()
