import csv

class ToDoList:
    
    
    def __init__(self):
        self.tasks = []
    
    # CREATE
    def add_task(self, task):
        self.tasks.append(task)
    
    # READ
    def show_tasks(self):
        for index, task in enumerate(self.tasks, 1):
            print(index, task)
    
    # DELETE
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
            

    # MARK DONE
    def mark_done(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_done()
                print("Task completed")
                return
            
    # SAVE TO CSV
    def save_to_file(self, filename="data/tasks.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "description", "priority", "status"])
            
            for task in self.tasks:
                writer.writerow([
                    task.name,
                    task.description,
                    task.priority,
                    task.status
                ])
                
    # LOAD FROM CSV
    def load_from_file(self, filename="data/tasks.csv"):
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    from models.task import Task
                    
                    task = Task(
                        row["name"],
                        row["description"],
                        row["priority"],
                        row["status"],
                    )
                    
                    self.tasks.append(task)
                    
        except FileNotFoundError:
            self.tasks = []