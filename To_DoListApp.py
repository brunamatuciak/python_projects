from typing import List

class ToDo:
    def __init__(self, title, description, due_date):
        self.title = title;
        self.description = description;
        self.due_date = due_date;
        self.completed= False;
        self.tasks: List[ToDo] = [];

    def create_task(self, title: str, description: str, due_date: str) -> None:
        self.tasks.append(ToDo(title, description, due_date))

    def delete_task(self) -> None:
        self.tasks.remove(ToDo(self.title, self.description, self.due_date))

    def mark_completed(self) -> None:
        self.completed = True

    def list_tasks(self):
        return self.tasks


def runApp():

    while True:

        print("""
            ---------To-Do List App---------
              1. Create Task
              2. Delete Task
              3. Mark Task Completed
              4. List Tasks
              5. Exit
              """)
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date: ")
            new_task = ToDo(title, description, due_date)
            print("Task created successfully.")

        elif choice == 2:
            if new_task:
                new_task.delete_task(new_task)
                print("Task deleted successfully.")
            else:
                print("No task to delete.")

        elif choice == 3:
            if new_task:
                new_task.mark_completed(new_task)
                print("Task marked as completed.")
            else:
                print("No task to mark as completed.")

        elif choice == 4:
            if new_task:
                tasks = [new_task]
                for task in new_task.list_tasks(tasks):
                    status = "Completed" if task.completed else "Pending"
                    print(f"Title: {task.title}, Description: {task.description}, Due Date: {task.due_date}, Status: {status}")
            else:
                print("No tasks available.")
        elif choice == 5:
            print("Exiting the To-Do List App.")
            break

runApp()