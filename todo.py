from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False


tasks = []


def add_task(title):
    tasks.append(Task(len(tasks) + 1, title))


def list_tasks():
    for t in tasks:
        print(f"[{'x' if t.done else ' '}] {t.id}. {t.title}")


def complete_task(task_id):
    for t in tasks:
        if t.id == task_id:
            t.done = True


def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t.id != task_id]
