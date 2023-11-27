import json

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        # Initialize an empty list to store tasks
        self.tasks = []

    # Function to add a task to the list
    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    # Function to delete a task
    def delete_task(self, task_index):
        deleted_task = self.tasks.pop(task_index)
        print(f'Task "{deleted_task.title}" deleted successfully!')

    # Function to display tasks
    def view_tasks(self):
        if not self.tasks:
            print("Oops! The task list is empty. Add some tasks first.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. Title: {task.title}, Description: {task.description}, Status: {task.status}")

    # Function to save the list of tasks to a file
    def save_tasks(self, file_name="tasks.json"):
        with open(file_name, 'w') as file:
            tasks_data = [{'title': task.title, 'description': task.description, 'status': task.status} for task in self.tasks]
            json.dump(tasks_data, file)
        print("Tasks saved successfully!")

    # Function to load the list of tasks from a file
    def load_tasks(self, file_name="tasks.json"):
        try:
            with open(file_name, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task['title'], task['description'], task['status']) for task in tasks_data]
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("No saved tasks found.")

# Create an instance of ToDoList
to_do_list = ToDoList()

# Main loop
while True:
    print("╔══════════════════════════════════════════╗")
    print("║             TO-DO LIST APP               ║")
    print("╚══════════════════════════════════════════╝")
    print('1. Add a New Task')
    print('2. Delete Task')
    print('3. View Task List')
    print('4. Save Tasks')
    print('5. Load Tasks')
    print('6. Exit')

    choice = input('Enter the number for the option to be chosen: ')

    if choice == '1':
        title = input('Enter the title for the task: ')
        description = input('Enter the description for the task: ')
        new_task = Task(title, description)
        to_do_list.add_task(new_task)

    elif choice == '2':
        to_do_list.view_tasks()
        task_index = int(input('Enter the task index to delete: ')) - 1
        if 0 <= task_index < len(to_do_list.tasks):
            to_do_list.delete_task(task_index)
        else:
            print('Invalid index. Task not deleted.')

    elif choice == '3':
        to_do_list.view_tasks()

    elif choice == '4':
        to_do_list.save_tasks()

    elif choice == '5':
        to_do_list.load_tasks()

    elif choice == '6':
        print('Thanks for using To-Do List. Goodbye!')
        break

    else:
        print('Oops! That\'s an invalid choice. Please select a valid option.')


