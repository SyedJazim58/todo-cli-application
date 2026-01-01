import inquirer
from rich.console import Console
from rich.table import Table
from todo_cli.services.task_service import TaskService

console = Console()
service = TaskService()

def add_task_flow():
    """US1: Add task flow with interactive prompts"""
    questions = [
        inquirer.Text('title', message="Enter task title"),
        inquirer.Text('description', message="Enter task description (optional)")
    ]
    answers = inquirer.prompt(questions)

    if not answers:
        return

    try:
        task = service.add_task(answers['title'], answers['description'])
        console.print(f"[green]Successfully added task: {task.title}[/green]")
    except ValueError as e:
        console.print(f"[red]Error: {str(e)}[/red]")

def view_tasks_flow():
    """US2: View task list with rich formatting"""
    tasks = service.get_all_tasks()

    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return

    table = Table(title="Todo List")
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Status", style="magenta")
    table.add_column("Title", style="green")
    table.add_column("Description", style="white")

    for task in tasks:
        status = "[green]✓[/green]" if task.completed else "[red] [/red]"
        table.add_row(task.id[:8], status, task.title, task.description)

    console.print(table)

def mark_task_flow():
    """US3: Mark task as complete/incomplete"""
    tasks = service.get_all_tasks()
    if not tasks:
        console.print("[yellow]No tasks to mark.[/yellow]")
        return

    choices = [
        (f"{'[✓] ' if t.completed else '[ ] '} {t.title}", t.id)
        for t in tasks
    ]
    choices.append(('Cancel', 'cancel'))

    questions = [
        inquirer.List('task_id', message="Select task to toggle status", choices=choices)
    ]
    answers = inquirer.prompt(questions)

    if not answers or answers['task_id'] == 'cancel':
        return

    task_id = answers['task_id']
    task = service.get_task_by_id(task_id)

    if task.completed:
        service.mark_task_incomplete(task_id)
        console.print(f"[yellow]Marked '{task.title}' as incomplete.[/yellow]")
    else:
        service.mark_task_complete(task_id)
        console.print(f"[green]Marked '{task.title}' as complete.[/green]")

def update_task_flow():
    """US4: Update task details"""
    tasks = service.get_all_tasks()
    if not tasks:
        console.print("[yellow]No tasks to update.[/yellow]")
        return

    choices = [(t.title, t.id) for t in tasks]
    choices.append(('Cancel', 'cancel'))

    questions = [
        inquirer.List('task_id', message="Select task to update", choices=choices)
    ]
    answers = inquirer.prompt(questions)

    if not answers or answers['task_id'] == 'cancel':
        return

    task_id = answers['task_id']
    task = service.get_task_by_id(task_id)

    update_questions = [
        inquirer.Text('title', message="New title (leave blank to keep current)", default=task.title),
        inquirer.Text('description', message="New description (leave blank to keep current)", default=task.description)
    ]
    updates = inquirer.prompt(update_questions)

    if not updates:
        return

    try:
        service.update_task(task_id, title=updates['title'], description=updates['description'])
        console.print(f"[green]Successfully updated task: {updates['title']}[/green]")
    except ValueError as e:
        console.print(f"[red]Error: {str(e)}[/red]")

def delete_task_flow():
    """US5: Delete task with confirmation"""
    tasks = service.get_all_tasks()
    if not tasks:
        console.print("[yellow]No tasks to delete.[/yellow]")
        return

    choices = [(t.title, t.id) for t in tasks]
    choices.append(('Cancel', 'cancel'))

    questions = [
        inquirer.List('task_id', message="Select task to delete", choices=choices)
    ]
    answers = inquirer.prompt(questions)

    if not answers or answers['task_id'] == 'cancel':
        return

    task_id = answers['task_id']
    task = service.get_task_by_id(task_id)

    confirm = inquirer.prompt([
        inquirer.Confirm('delete', message=f"Are you sure you want to delete '{task.title}'?", default=False)
    ])

    if confirm and confirm['delete']:
        service.delete_task(task_id)
        console.print(f"[red]Successfully deleted task: {task.title}[/red]")

def main():
    """Main application loop"""
    while True:
        console.print("\n[bold blue]Todo CLI[/bold blue]")
        questions = [
            inquirer.List('action',
                          message="What would you like to do?",
                          choices=[
                              ('View Tasks', 'view'),
                              ('Add Task', 'add'),
                              ('Mark Complete/Incomplete', 'mark'),
                              ('Update Task', 'update'),
                              ('Delete Task', 'delete'),
                              ('Exit', 'exit')
                          ])
        ]
        answers = inquirer.prompt(questions)

        if not answers or answers['action'] == 'exit':
            console.print("Goodbye!")
            break

        if answers['action'] == 'add':
            add_task_flow()
        elif answers['action'] == 'view':
            view_tasks_flow()
        elif answers['action'] == 'mark':
            mark_task_flow()
        elif answers['action'] == 'update':
            update_task_flow()
        elif answers['action'] == 'delete':
            delete_task_flow()

if __name__ == "__main__":
    main()
