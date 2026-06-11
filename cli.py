from service import TaskManagerService


# Shows all commands the user can run.
def show_menu():
    print("\nCommands:")
    print("add_user")
    print("add_project")
    print("update_status")
    print("add_task")
    print("view_all")
    print("exit")


# Starts the command-line interface.
def run_cli():
    service = TaskManagerService()

    while True:
        show_menu()
        command = input("\nEnter command: ")

        # Create a new user.
        if command == "add_user":
            user_id = input("User ID: ")
            name = input("Name: ")
            service.add_user(user_id, name)
            print("User added!")

        # Add a project to an existing user.
        elif command == "add_project":
            user_id = input("User ID: ")
            project_id = input("Project ID: ")
            name = input("Project Name: ")
            service.add_project(user_id, project_id, name)
            print("Project added!")

        # Update a project status to In Progress or Completed.
        elif command == "update_status":
            user_id = input("User ID: ")
            project_id = input("Project ID: ")
            print("Choose status:")
            print("1. In Progress")
            print("2. Completed")
            status = input("New Project Status: ")
            project = service.update_project_status(user_id, project_id, status)
            if project:
                print("Project status updated!")
            else:
                print("Project not found or invalid status.")

        # Add a task to an existing project.
        elif command == "add_task":
            user_id = input("User ID: ")
            project_id = input("Project ID: ")
            task_id = input("Task ID: ")
            title = input("Task Title: ")
            service.add_task(user_id, project_id, task_id, title)
            print("Task added!")

        # Display all users, projects, and tasks.
        elif command == "view_all":
            print(service.view())

        elif command == "exit":
            break

        else:
            print("Invalid command")


if __name__ == "__main__":
    run_cli()
