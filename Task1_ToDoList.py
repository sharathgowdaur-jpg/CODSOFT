tasks=[]

def show_task():
    if len(tasks)==0:
        print("Your Task list is empty!")
    else:
        print("Your task list is :")
        for i in range(len(tasks)):
            print(f"{i+1}.{tasks[i]}")

def add_task():
    task=input("enter your task to add in to do list:")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    show_task()
    if len(tasks)==0:
        print("No task to delete!")
        return
    try:
        num=int(input("enter the task number to delete:"))
        if 1<=num<=len(tasks):
            tasks.pop(num-1)
            print(f"Your task {num} is deleted successfully!")
        else:
            print("You entered task number is does not exist! please eneter valid task number!")
    except:
        print("Invalid input! please enter a valid task number!")

def update_task():
    show_task()
    if len(tasks)==0:
        print("No task to update!")
        return
    try:
        num=int(input("enter the task number to update:"))
        if 1<=num<=len(tasks):
            new_task=input("enter the new task:")
            tasks[num-1]=new_task
            print(f"Your task {num} is updated successfully!")
        else:
            print("You entered task number is does not exist! please eneter valid task number!")
    except:
        print("Invalid input! please enter a valid task number!")

while True:
    print("===========To do list menu from codsoft==========")
    print("1.show task")
    print("2.add task")
    print("3.delete task")
    print("4.update task")
    print("5.exit")

    choice=int(input("enter your choice:"))
    if choice==1:
        show_task()
    elif choice==2:
        add_task()
    elif choice==3:
        delete_task()
    elif choice==4:
        update_task()
    elif choice==5:
        print("Exiting the to-do list. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
