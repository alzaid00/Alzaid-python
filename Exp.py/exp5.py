
#Program 4: Task List Manager
# mutable tasks
tasks = []

# Function to add task
def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added!")

# functions to remove task
def remove_task():
    task = input("Enter the task you want to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed succesfully!")
    else:
        print("Task not found")

# function to update task
def update_task():
    old_task = input("Enter the task you want to update: ")
    if old_task in tasks:
        new_task = input("Enter the new task: ")
        index = tasks.index(old_task)
        tasks[index] = new_task
        print("Task Updated!")
    else:
        print("Task not found!")

# Display tasks
def display_tasks():
    print("\nTask List:")
    for task in tasks:
        print("-", task)

#sorting tasks
def sort_task():
    tasks.sort()
    print("Tasks sorted!")

while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Update Task")
    print("4. Display Task")
    print("5. Sort Task")

    choice = int(input("Enter your choice (1-5) "))

    if choice == 1:
        add_task()
    elif choice == 2:
        remove_task()
    elif choice == 3:
        update_task()
    elif choice == 4:
        display_tasks()
    elif choice == 5:
        update_task()
