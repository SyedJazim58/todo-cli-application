# Data Model: Basic Todo CLI App

## Entity: Task

**Fields**:
- `id`: int (unique identifier, auto-incremented)
- `title`: str (required, maximum 100 characters)
- `description`: str (optional, maximum 1000 characters)
- `completed`: bool (default False)
- `created_at`: datetime (automatically set on creation)
- `updated_at`: datetime (automatically updated on modifications)

**Validation Rules**:
- Title must not be empty or only whitespace
- Title length must be between 1 and 100 characters
- Description length must not exceed 1000 characters if provided
- ID must be unique within the task collection

**State Transitions**:
- New Task: `completed = False` by default
- Mark Complete: `completed = True`
- Mark Incomplete: `completed = False`

## Entity: TaskList

**Fields**:
- `tasks`: List[Task] (collection of Task objects)
- `next_id`: int (auto-incremented counter for new task IDs)

**Operations**:
- Add Task: Add a new task to the collection
- Get All Tasks: Return all tasks in the collection
- Get Task by ID: Return specific task by its ID
- Update Task: Modify an existing task by ID
- Delete Task: Remove a task by ID
- Mark Complete: Update completion status by ID