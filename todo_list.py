tasks = []
completed_tasks = []

while True:
    print("To-Do List:")
    i = 1
    for task in tasks:
        status = "(Completed)" if task in completed_tasks else ""
        print(f"{i}. {task} {status}")
        i += 1
    
    print("Options:")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks += [task]
    elif choice == "2":
        print("All Tasks:")
        i = 1
        for task in tasks:
            status = "(Completed)" if task in completed_tasks else ""
            print(f"{i}. {task} {status}")
            i += 1
    elif choice == "3":
        index = int(input("Enter task number to mark as completed: "))
        if 1 <= index <= len(tasks):
            completed_tasks += [tasks[index - 1]]
        else:
            print("Invalid task number.")
    elif choice == "4":
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            task_to_remove = tasks[index - 1]
            tasks_copy = []
            for i in range(len(tasks)):
                if i != index - 1:
                    tasks_copy.append(tasks[i])
            tasks = tasks_copy
            completed_tasks_copy = []
            for task in completed_tasks:
                if task != task_to_remove:
                    completed_tasks_copy.append(task)
            completed_tasks = completed_tasks_copy
        else:
            print("Invalid task number.")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")
