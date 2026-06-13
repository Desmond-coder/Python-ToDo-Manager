from models.task import Task
from services.todo_list import ToDoList

todo = ToDoList()
todo.load_from_file()

while True:
    print("\n===== To DO LIST =====")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Mark as Done")
    print("5. Save")
    print("6. Exit")
    
    choice = input("choose an option: ")
    
    if choice == "1":
        name = input("Task name: ")
        desc = input("Description: ")
        priority = input("Priority (low/medium/high): ")
        
        task = Task(name, desc, priority)
        todo.add_task(task)
        
    elif choice == "2":
        todo.show_tasks()
        
    elif choice == "3":
        name = input("which task do you want to delete?")
        todo.delete_task(name)
        
    elif choice == "4":
        name = input("Task name to complete: ")
        todo.mark_done(name)
        
    elif choice == "5":
        todo.save_to_file()
        print("Saved successfully")
        
    elif choice == "6":
        todo.save_to_file()
        print("Exiting...")
        break
    
    else:
        print("Invalid option")