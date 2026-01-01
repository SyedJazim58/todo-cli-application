from typing import List, Optional
from todo_cli.models.task import Task, TaskList

class TaskService:
    """
    Service class handling business logic for task management.
    """
    def __init__(self):
        self._task_list = TaskList()

    def add_task(self, title: str, description: str = "") -> Task:
        task = Task(title, description)
        self._task_list.add(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        return self._task_list.get_all()

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        return self._task_list.get(task_id)

    def update_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        task = self.get_task_by_id(task_id)
        if not task:
            raise KeyError(f"Task with ID {task_id} not found")
        task.update(title, description)
        return task

    def delete_task(self, task_id: str):
        self._task_list.remove(task_id)

    def mark_task_complete(self, task_id: str) -> Task:
        task = self.get_task_by_id(task_id)
        if not task:
            raise KeyError(f"Task with ID {task_id} not found")
        task.mark_complete()
        return task

    def mark_task_incomplete(self, task_id: str) -> Task:
        task = self.get_task_by_id(task_id)
        if not task:
            raise KeyError(f"Task with ID {task_id} not found")
        task.mark_incomplete()
        return task
