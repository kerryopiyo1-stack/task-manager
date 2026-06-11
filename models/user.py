class User:
    def __init__(self, user_id_or_name, name=None):
        if name is None:
            self.user_id = None
            self.name = user_id_or_name
        else:
            self.user_id = user_id_or_name
            self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)
