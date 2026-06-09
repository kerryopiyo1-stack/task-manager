import json

FILE_PATH = 'data/data.json'

def load_data():
    try:
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"users": []}  

def save_data(data):
    with open(FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)