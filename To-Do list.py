tasks = []

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
    
    choice = input("Choose: ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")
        
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
                
    elif choice == "3":
        task_number = int(input("Task number to remove: "))
        if task_number >= 1 and task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task removed")
        else:
            print("Invalid task number.")
            
    elif choice == "4":
        print("Goodbye!")
        break
else:
    print("Invalid option, try again.")