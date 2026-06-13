class Task:
    def __init__(self, name, description, priority, status="pending"):
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status
        
    def mark_done(self):
        self.status = "done"
        
    def __str__(self):
        return f"{self.name} | {self.description} | {self.priority} | {self.status}"
    
    