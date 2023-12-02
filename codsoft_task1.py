import os


class ToDoListApp:
    def __init__(self):
        self.tasks_list = []

    def clear_console(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def display_menu(self):
        self.clear_console()
        print("To-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark as Completed")
        print("4. Delete Task")
        print("5. Exit")

    def add_task(self):
        new_task = input("Enter a new task: ")
        self.tasks_list.append({"task": new_task, "completed": False})
        input("Task added. Press enter to continue...")

    def view_tasks(self):
        self.clear_console()
        print("To-Do List:")
        for i, task in enumerate(self.tasks_list, start=1):
            status = "Done" if task["completed"] else "Not done"
            print(f"{i}. {task['task']} - Status: {status}")
        input("Press enter to continue...")

    def mark_task_as_completed(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(self.tasks_list):
            self.tasks_list[task_number]["completed"] = True
            input("Task marked as completed. Press enter to continue...")
        else:
            input("Invalid task number. Press enter to continue...")

    def delete_selected_task(self):
        self.view_tasks()
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(self.tasks_list):
            del self.tasks_list[task_number]
            input("Task deleted. Press enter to continue...")
        else:
            input("Invalid task number. Press enter to continue...")

    def run(self):
        while True:
            self.display_menu()
            user_choice = input("Enter your choice (1/2/3/4/5): ")

            if user_choice == '1':
                self.add_task()
            elif user_choice == '2':
                self.view_tasks()
            elif user_choice == '3':
                self.mark_task_as_completed()
            elif user_choice == '4':
                self.delete_selected_task()
            elif user_choice == '5':
                exit()
                break
            else:
                print("Invalid choice. Press enter to continue...")


if __name__ == "__main__":
    todo_app = ToDoListApp()
    todo_app.run()
