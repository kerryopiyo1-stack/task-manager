class Task:
    def __init__(self, task_id, title, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.status = status

    def mark_as_completed(self):
        self.status = "Completed"

    def mark_as_pending(self):
        self.status = "Pending"

    def mark_as_in_progress(self):
        self.status = "In Progress"
