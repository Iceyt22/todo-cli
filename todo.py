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
