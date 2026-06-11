# Represents one task inside a project.
class Task:
    def __init__(self, task_id, title, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.status = status

    # Change the task status to completed.
    def mark_as_completed(self):
        self.status = "Completed"

    # Change the task status to pending.
    def mark_as_pending(self):
        self.status = "Pending"

    # Change the task status to in progress.
    def mark_as_in_progress(self):
        self.status = "In Progress"
