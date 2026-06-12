# Task Manager CLI Application

## Overview

This is a Command Line Interface (CLI) Task Management System built using Python and Object-Oriented Programming (OOP) principles.

The application allows administrators to manage users, projects, and tasks from the terminal.

## Features

- Add users
- Add projects to users
- Add tasks to projects
- View all users, projects, and tasks
- Update task status
- Store data in JSON format
- Command-line interface

## Project Structure

```text
task-manager/
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── project.py
│   └── task.py
│
├── data/
│   └── data.json
│
├── tests/
│   ├── test_user.py
│   └── test_task.py
│
├── cli.py
├── service.py
├── storage.py
├── main.py
├── requirements.txt
└── README.md
```

## Technologies Used

- Python 3
- OOP (Classes and Objects)
- JSON Storage
- Pytest

## Installation

### Clone the repository

```bash
git clone <your-repository-url>
cd task-manager
```

### Create a virtual environment

```bash
python3 -m venv virtual-env
```

### Activate the virtual environment

Linux/macOS:

```bash
source virtual-env/bin/activate
```

Windows:

```bash
virtual-env\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the application:

```bash
python3 main.py
```

or

```bash
python3 cli.py
```

## Available Commands

```text
add_user
add_project
add_task
view_all
update_task
exit
```

### Example

```text
Enter command: add_user
User ID: 1
Name: Kerry

Enter command: add_project
User ID: 1
Project ID: 101
Project Name: Python Project

Enter command: add_task
User ID: 1
Project ID: 101
Task ID: 201
Task Title: Build CLI
```

## Testing

Run all tests:

```bash
PYTHONPATH=. pytest -v
```

Expected output:

```text
tests/test_task.py::test_task_status PASSED
tests/test_user.py::test_user_creation PASSED
```

## OOP Concepts Used

### Encapsulation

Data and methods are grouped inside classes:

- User
- Project
- Task

### Composition

- A User owns Projects
- A Project owns Tasks

### Abstraction

The service layer hides the implementation details from the CLI.

## Author

Kerry Opiyo

