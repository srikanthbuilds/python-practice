print("-------- Student Task Manager --------")
tasks = []
task_no = 0
while True:
    print("1. Add Tasks\n2. View Tasks\n3. Mark task as completed\n4. Delete Task\n5. Exit")
    option = input("Enter options from (1,2,3,4,5): ")
    option = int(option)
    if option == 1 :
        task_no = int(input("Enter your task ID: "))
        task_name =  (input("Type your task name: "))
        task_status = (input("Enter your task status (pending / completed) : "))
        task = {
            "ID" : task_no,
            "NAME" :task_name,
            "STATUS" : task_status,
        }
        tasks.append(task)
        print()
    elif option == 2:
        print("--- Your tasks ---")
        for task in tasks:
            print(task["ID"]," - ",task["NAME"]," - ",task["STATUS"])
        print()
    elif option == 3:
        task_no = int(input("Enter your task ID to mark as completed : "))
        for task in tasks:
            if task["ID"] == task_no:
                task.update({"STATUS":"completed"})
                print(f"Task {task_no} marked as completed!")
                print()
                break
            else:
                print(f"Task {task_no} not found!")
                print()


    elif option == 4:
        task_no = int(input("Enter your task ID to delete : "))
        for task in tasks:
            if task["ID"] == task_no:
                tasks.remove(task)
                print(f"Task {task_no} deleted!")
                print()
                break
            else:
                print(f"Task {task_no} not found!")
                break
                print()
    elif option == 5:

        print("----- EXITED -----")
        break





