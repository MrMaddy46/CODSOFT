# To-Do List App

tasks = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(" Task added successfully!")

def view_tasks():
    if not tasks:
        print(" No tasks in the list.")
    else:
        print("\n Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_no - 1)
            print(f" Removed: {removed}")
        except (IndexError, ValueError):
            print(" Invalid input. Try again.")

while True:
    show_menu()
    choice = input("Choose an option (1–4): ")
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1–4.")
