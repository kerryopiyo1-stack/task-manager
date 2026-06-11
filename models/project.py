# Represents one project that belongs to a user.
class Project:
    def __init__(self, project_id, name, status="Pending"):
        self.project_id = project_id
        self.name = name
        self.status = status
        # A project can have many tasks.
        self.tasks = []

    # Change the project status to completed.
    def mark_as_completed(self):
        self.status = "Completed"

    # Change the project status to pending.
    def mark_as_pending(self):
        self.status = "Pending"

    # Change the project status to in progress.
    def mark_as_in_progress(self):
        self.status = "In Progress"
