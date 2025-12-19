import os
TASK_FILE = "task.txt"

def load_tasks():
    tasks = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            for line in f:
                text, status = line.strip().rsplit(" || ", 1) #rsplit = split from right side, 1 = one splitting i.e two parts is what we get

                tasks.append({"text": text, "done": status == "done"}) #complicated line, DIY (decode it yourself)

                """tasks = [
    {"text": "Buy milk", "done": True},
    {"text": "Clean room", "done": False},
    {"text": "Study python", "done": True}
]
"""
    return tasks



def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding = "utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not done"
            f.write(f"{task['text']} || {status}\n")


def display_tasks(tasks):
    if not tasks:
        print(f"No tasks Found ")
    else:
        for i, task in enumerate(tasks, 1):
            checkbox = "✅" if task["done"] else ""
            print(f"{i}, [{checkbox}] {task['text']}")
    print()


def task_manager():
    tasks = load_tasks()

    while True:
        print("\n-------------Task List Manager-------------")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task")
        print("4. Delete Task")
        print("5. Exit")

        choice= input("Choose an option (1-5)  ").strip()
        match choice:
            case "1": 
                text = input("Enter your task ").strip()
                if text:
                    tasks.append({"text": text, "done": False})
                    save_tasks(tasks)
                else:
                    print("Task cannot be empty ")
            case "2":
                display_tasks(tasks)
            case "3": 
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number: "))
                    if 1 <= num <= len(tasks):
                        tasks[num-1]["done"] = True
                        save_tasks(tasks)
                        print("Task marked as DONE ")
                    else:
                        print("Invalid task number ")
                except ValueError:
                    print("Please enter a number! ")
            case "4": 
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number: "))
                    if 1 <= num <= len(tasks):
                        tasks.pop(num-1)
                        save_tasks(tasks)
                        print("Task removed ")
                    else:
                        print("Invalid task number ")
                except ValueError:
                    print("Please enter a number! ")
            case "5":
                print("Exiting Task Manager ")
                break
            case _:
                print("Please choose a valid option. ")

task_manager()
