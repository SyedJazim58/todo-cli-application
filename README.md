# Todo CLI Application

A simple, interactive command-line todo application built with Python.

## Features

- **Add Tasks**: Create new tasks with title and optional description.
- **View Tasks**: Display all tasks in a formatted table with status indicators.
- **Mark Complete/Incomplete**: Toggle the completion status of your tasks.
- **Update Tasks**: Modify existing task titles and descriptions.
- **Delete Tasks**: Remove tasks from your list with confirmation.

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) (recommended package manager)

## Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

Run the application using uv:
```bash
PYTHONPATH=src uv run python src/todo_cli/cli/main.py
```

## Running Tests

Run the test suite with pytest:
```bash
uv run pytest
```

## Project Structure

- `src/todo_cli/`: Application source code.
  - `models/`: Data models for Tasks and TaskList.
  - `services/`: Business logic layer.
  - `cli/`: Interactive command-line interface.
- `tests/`: Unit and integration tests.
