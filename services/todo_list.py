class ToDoList:
    
    
    def __init__(self):
        self.tasks = []
    
    
    def add_task(self, task):
        self.tasks.append(task)
    
    
    def show_tasks(self):
        for index, task in enumerate(self.tasks, 1):
            print(index, task)
    
    
    def delete_task(self, task_name):
        found = False
        for task in self.tasks:
            if task.name == task_name:
                found = True
                self.tasks.remove(task)
                print("Task deleted")
                break
        if not found:
            print("There is no such task")