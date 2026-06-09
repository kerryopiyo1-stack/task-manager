class Project:
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
