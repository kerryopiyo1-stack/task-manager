from models.task import Task
from service import TaskManagerService
from utils import storage

def test_task_status():
    task = Task("t1", "Learn Python")

    assert task.status == "Pending"

    task.mark_as_completed()
    assert task.status == "Completed"


def test_delete_task(tmp_path, monkeypatch):
    test_file = tmp_path / "data.json"
    test_file.write_text("[]")
    monkeypatch.setattr(storage, "FILE_PATH", str(test_file))

    service = TaskManagerService()
    service.add_user("1", "Kerry")
    service.add_project("1", "p1", "Python")
    service.add_task("1", "p1", "t1", "Learn Python")

    deleted_task = service.delete_task("1", "p1", "t1")

    assert deleted_task.title == "Learn Python"
    assert service.users[0].projects[0].tasks == []
