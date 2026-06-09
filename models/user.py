class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)