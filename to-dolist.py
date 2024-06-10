import os

# Define the file name to store the tasks
FILE_NAME = "tasks.txt"

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f'Task "{task}" added.')

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        for task in tasks:
            file.write(task + "\n")
    print(f"Tasks saved to {FILE_NAME}.")

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        print(f"Tasks loaded from {FILE_NAME}.")
    else:
        print(f"No saved tasks found ({FILE_NAME} not found).")
    return tasks

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
        elif choice == "5":
            tasks = load_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()

