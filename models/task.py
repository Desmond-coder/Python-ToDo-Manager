class Task:
    def __init__(self, name, description, priority, status="pending"):
        self.name = name
        self.description = description
        self.priority = priority
        self.status = status