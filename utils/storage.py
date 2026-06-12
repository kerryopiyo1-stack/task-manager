import json
import os

# File where all saved users, projects, and tasks are stored.
FILE_PATH = "data/data.json"


# Read saved data from the JSON file.
def load_data():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        # Empty files should behave like no saved data.
        if os.path.getsize(FILE_PATH) == 0:
            return []
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


# Save data back to the JSON file.
def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
