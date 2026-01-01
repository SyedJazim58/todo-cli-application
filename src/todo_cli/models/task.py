from datetime import datetime
import uuid
from typing import Optional, List, Dict

class Task:
    """
    Task model class representing a single todo item.
    """
    def __init__(self, title: str, description: str = "", task_id: Optional[str] = None):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        self.id = task_id or str(uuid.uuid4())
        self.title = title.strip()
        self.description = description.strip()
        self.completed = False
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def mark_complete(self):
        self.completed = True
        self.updated_at = datetime.now()

    def mark_incomplete(self):
        self.completed = False
        self.updated_at = datetime.now()

    def update(self, title: Optional[str] = None, description: Optional[str] = None):
        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            self.title = title.strip()
        if description is not None:
            self.description = description.strip()
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

class TaskList:
    """
    TaskList model class to manage a collection of Task objects in memory.
    """
    def __init__(self):
        self._tasks: Dict[str, Task] = {}

    def add(self, task: Task):
        self._tasks[task.id] = task

    def get(self, task_id: str) -> Optional[Task]:
        return self._tasks.get(task_id)

    def get_all(self) -> List[Task]:
        return list(self._tasks.values())

    def remove(self, task_id: str):
        if task_id in self._tasks:
            del self._tasks[task_id]
        else:
            raise KeyError(f"Task with ID {task_id} not found")
