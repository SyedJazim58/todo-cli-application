import pytest
from todo_cli.models.task import Task

def test_task_creation_valid():
    """T015: Unit test for Task creation with valid title"""
    task = Task(title="Buy milk", description="Get full cream milk")
    assert task.title == "Buy milk"
    assert task.description == "Get full cream milk"
    assert task.completed is False
    assert task.id is not None
    assert task.created_at == task.updated_at

def test_task_creation_empty_title():
    """T016: Unit test for Task validation (empty title rejection)"""
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task(title="")

def test_task_creation_whitespace_title():
    """Additional test: whitespace only title rejection"""
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task(title="   ")
