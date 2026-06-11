from models.task import Task

def test_task_status():
    task = Task("t1", "Learn Python")

    assert task.status == "Pending"

    task.mark_as_completed()
    assert task.status == "Completed"