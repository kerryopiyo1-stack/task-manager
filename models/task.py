class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_as_completed(self):
        self.completed = True
    