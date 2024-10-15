import json
import os

class TodoList:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for idx, task in enumerate(self.tasks):
            status = "✓" if task['completed'] else "✗"
            print(f"{idx + 1}. {task['task']} [{status}]")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
            print(f"Task '{self.tasks[task_index]['task']}' marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"Task '{removed_task['task']}' has been deleted.")
        else:
            print("Invalid task number.")

def main():
    todo = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            if task.strip():
                todo.add_task(task)
                print(f"Task '{task}' added.")
            else:
                print("Task cannot be empty.")
        elif choice == '2':
            print("\nYour Tasks:")
            todo.show_tasks()
        elif choice == '3':
            todo.show_tasks()
            try:
                index = int(input("Enter task number to complete: ")) - 1
                todo.complete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            todo.show_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                todo.delete_task(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
