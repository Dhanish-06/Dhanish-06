tasks = []


def addTask():
    task = input("Please enter a task")
    tasks.append(task)
    print(f"tasks: {task} added to list")


def listTask():
    if not tasks:
        print(" there are no tasks ")
    else:
        print("the tasks are: ")
        for index, task in enumerate(tasks):
            print(f"{index} -{task}")


def deleteTask():
    listTask()
    try:
        taskTodelete = int(input("Enter your choice: "))
        if taskTodelete >= 0  and taskTodelete< len(tasks):
            tasks.pop(taskTodelete)
            print(f"the give Task: {taskTodelete} has deleted")
        else:
            print(f"the give Task: {taskTodelete} is invalid")
    except:
            print("Invalid Input")


if __name__ == "__main__":
    print("welcome to-do-list app : ")
    while True:
        print("\n")
        print("Plese select one of the following options")
        print("-----------------------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. View all the Tasks")
        print("4. Exit")
        print("------------------------------------------")

        choice = int(input("Enter your choice:"))
        if choice == 1:
            addTask()
        elif choice == 2:
           deleteTask()
        elif choice == 3:
            listTask()
        elif choice == 4:
            break
        else:
            print("invalid choice")
             


