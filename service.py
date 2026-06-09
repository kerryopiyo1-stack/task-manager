from models.user import user
from models.task import task
from models.project import project
from utils.storage import storage

class TaskManagerService:
    def__init__(self):
     self.data = load_data()
    
    def add_user(self, user_id, name):
       self.data['users'].append({
            "user_id": user_id,
            "name": name,
            "projects": []
        })
        save_data(self.data)
       
       
