import pytest
from todo_cli.services.task_service import TaskService
from todo_cli.models.task import Task

def test_get_all_tasks_empty():
    """T022: Unit test for get_all_tasks (empty list)"""
    service = TaskService()
    assert service.get_all_tasks() == []

def test_get_all_tasks_with_data():
    """T022: Unit test for get_all_tasks (with data)"""
    service = TaskService()
    service.add_task("Task 1")
    service.add_task("Task 2")
    tasks = service.get_all_tasks()
    assert len(tasks) == 2
    assert any(t.title == "Task 1" for t in tasks)
    assert any(t.title == "Task 2" for t in tasks)

def test_mark_task_complete():
    """T029: Unit test for mark_task_complete functionality"""
    service = TaskService()
    task = service.add_task("Test")
    assert task.completed is False
    service.mark_task_complete(task.id)
    assert task.completed is True

def test_mark_task_incomplete():
    """T030: Unit test for mark_task_incomplete functionality"""
    service = TaskService()
    task = service.add_task("Test")
    service.mark_task_complete(task.id)
    assert task.completed is True
    service.mark_task_incomplete(task.id)
    assert task.completed is False

def test_update_task_details():
    """T036: Unit test for update_task functionality"""
    service = TaskService()
    task = service.add_task("Original Title", "Original Desc")
    service.update_task(task.id, title="New Title", description="New Desc")
    assert task.title == "New Title"
    assert task.description == "New Desc"

def test_update_task_partial():
    """T036: Test partial update (title only)"""
    service = TaskService()
    task = service.add_task("Original Title", "Original Desc")
    service.update_task(task.id, title="New Title")
    assert task.title == "New Title"
    assert task.description == "Original Desc"

def test_delete_task():
    """T043: Unit test for delete_task functionality"""
    service = TaskService()
    task = service.add_task("To Delete")
    assert len(service.get_all_tasks()) == 1
    service.delete_task(task.id)
    assert len(service.get_all_tasks()) == 0

def test_delete_non_existent_task():
    """T044: Test for delete validation (non-existent task handling)"""
    service = TaskService()
    with pytest.raises(KeyError):
        service.delete_task("invalid-id")
