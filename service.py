from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_data, save_data


# Handles the main task manager logic.
class TaskManagerService:
    # Project statuses do not include Pending when updating from the CLI.
    VALID_PROJECT_STATUSES = {
        "1": "In Progress",
        "2": "Completed",
        "completed": "Completed",
        "complete": "Completed",
        "done": "Completed",
        "in progress": "In Progress",
        "in_progress": "In Progress",
        "progress": "In Progress",
    }

    def __init__(self):
        # Load saved users when the app starts.
        self.users = self._load_users()

    # Add a new user and save it.
    def add_user(self, user_id, name):
        user = User(user_id, name)
        self.users.append(user)
        self._save_users()
        return user   
    
    def get_users(self):
        return self.users

    # Build the text shown by the view_all command.
    def view(self):
        if not self.users:
            return "No users found."

        lines = []
        for user in self.users:
            lines.append(f"User {user.user_id}: {user.name}")

            for project in user.projects:
                lines.append(
                    f"  Project {project.project_id}: {project.name} [{project.status}]"
                )

                for task in project.tasks:
                    lines.append(
                        f"    Task {task.task_id}: {task.title}"
                    )

        return "\n".join(lines)

    # Add a project to an existing user.
    def add_project(self, user_id, project_id, name):
        user = self._find_user(user_id)
        if user:
            project = Project(project_id, name)
            user.projects.append(project)
            self._save_users()
            return project

    # Update a project status to In Progress or Completed.
    def update_project_status(self, user_id, project_id, status):
        project = self._find_project(user_id, project_id)
        if project:
            status = self._format_project_status(status)
            if not status:
                return None
            if status == "Completed":
                project.mark_as_completed()
            elif status == "In Progress":
                project.mark_as_in_progress()
            self._save_users()
            return project

    # Add a task to an existing project.
    def add_task(self, user_id, project_id, task_id, title):
        project = self._find_project(user_id, project_id)
        if project:
            task = Task(task_id, title)
            project.tasks.append(task)
            self._save_users()
            return task

    # Delete an existing user and all their projects and tasks.
    def delete_user(self, user_id):
        user = self._find_user(user_id)
        if user:
            self.users.remove(user)
            self._save_users()
            return user

    # Delete an existing project and all its tasks.
    def delete_project(self, user_id, project_id):
        project = self._find_project(user_id, project_id)
        if project:
            user = self._find_user(user_id)
            user.projects.remove(project)
            self._save_users()
            return project

    # Delete an existing task.
    def delete_task(self, user_id, project_id, task_id):
        task = self._find_task(user_id, project_id, task_id)
        if task:
            project = self._find_project(user_id, project_id)
            project.tasks.remove(task)
            self._save_users()
            return task

    # Update a task status.
    def update_task_status(self, user_id, project_id, task_id, status):
        task = self._find_task(user_id, project_id, task_id)
        if task:
            status = status.strip().lower()
            if status in ["completed", "complete", "done"]:
                task.mark_as_completed()
            elif status == "pending":
                task.mark_as_pending()
            elif status in ["in progress", "in_progress", "progress"]:
                task.mark_as_in_progress()
            else:
                return None
            self._save_users()
            return task

    # Find a user by ID.
    def _find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    # Find a project by user ID and project ID.
    def _find_project(self, user_id, project_id):
        user = self._find_user(user_id)
        if user:
            for project in user.projects:
                if project.project_id == project_id:
                    return project
        return None

    # Find a task by user ID, project ID, and task ID.
    def _find_task(self, user_id, project_id, task_id):
        project = self._find_project(user_id, project_id)
        if project:
            for task in project.tasks:
                if task.task_id == task_id:
                    return task
        return None

    # Convert project status input into a saved status value.
    def _format_project_status(self, status):
        return self.VALID_PROJECT_STATUSES.get(status.strip().lower())

    # Convert JSON data into User, Project, and Task objects.
    def _load_users(self):
        data = load_data()

        if isinstance(data, dict) and "user" in data:
            data = [data["user"]]

        users = []
        for user_data in data:
            user = User(user_data["user_id"], user_data["name"])

            for project_data in user_data.get("projects", []):
                project = Project(
                    project_data["project_id"],
                    project_data["name"],
                    project_data.get("status", "Pending"),
                )

                for task_data in project_data.get("tasks", []):
                    task = Task(
                        task_data["task_id"],
                        task_data["title"],
                        task_data.get("status", "Pending"),
                    )
                    project.tasks.append(task)

                user.projects.append(project)

            users.append(user)

        return users

    # Convert User, Project, and Task objects into JSON data.
    def _save_users(self):
        data = []
        for user in self.users:
            data.append(
                {
                    "user_id": user.user_id,
                    "name": user.name,
                    "projects": [
                        {
                            "project_id": project.project_id,
                            "name": project.name,
                            "status": project.status,
                            "tasks": [
                                {
                                    "task_id": task.task_id,
                                    "title": task.title,
                                    "status": task.status,
                                }
                                for task in project.tasks
                            ],
                        }
                        for project in user.projects
                    ],
                }
            )

        save_data(data)


TaskManager = TaskManagerService
