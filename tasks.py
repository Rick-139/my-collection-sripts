import os

def load_tasks(filename):
    """Load tasks from a file."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(filename, tasks):
    """Save tasks to a file."""
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(filename, tasks)
            print(f'Task "{task}" added.')

        elif choice == '2':
            display_tasks(tasks)

        elif choice == '3':
            display_tasks(tasks)
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    save_tasks(filename, tasks)
                    print(f'Task "{removed_task}" removed.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
