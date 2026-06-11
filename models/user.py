# Represents one user in the task manager.
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        # A user can have many projects.
        self.projects = []
