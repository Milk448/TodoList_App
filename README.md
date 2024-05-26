#Name :Milko Shuma  Id UGR/4707/13
#section 2

# To-Do List Application

A simple To-Do List application implemented in Python, using a linked list to manage tasks. This application allows users to add tasks, mark them as completed, and view the list of tasks.

## Features

- **Add Tasks**: Add new tasks to the to-do list with a title and description.
- **Mark Tasks as Completed**: Mark tasks as completed based on their title.
- **View Tasks**: Display the list of tasks, including their completion status.

## Project Structure


## Classes and Methods

### Task Class

- **Attributes**:
  - `title`: The title of the task.
  - `description`: The description of the task.
  - `completed`: A boolean indicating whether the task is completed or not.

- **Methods**:
  - `__init__(self, title, description)`: Constructor to initialize a task with a title and description.
  - `get_title(self)`: Getter method to retrieve the title of the task.
  - `get_description(self)`: Getter method to retrieve the description of the task.
  - `is_completed(self)`: Getter method to check if the task is completed.
  - `mark_completed(self)`: Method to mark the task as completed.

### Node Class

- **Attributes**:
  - `task`: Reference to a Task.
  - `next`: Reference to the next Node in the linked list.

- **Methods**:
  - `__init__(self, task)`: Constructor to initialize a node with a task.

### ToDoList Class

- **Attributes**:
  - `head`: Reference to the head Node of the linked list.

- **Methods**:
  - `__init__(self)`: Constructor to initialize an empty to-do list.
  - `add_to_do(self, task)`: Method to add a new task to the to-do list.
  - `mark_to_do_as_completed(self, title)`: Method to mark a task as completed based on its title.
  - `view_to_do_list(self)`: Method to display the list of tasks in the to-do list.

## Usage

### Running the Application

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ToDoList_App
