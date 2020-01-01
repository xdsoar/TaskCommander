# coding=utf-8
from typing import List

from taskcommander.domain.task import Task
from taskcommander.service.task_repo import TaskRepo


class TaskService:
    task_repo: TaskRepo

    def __init__(self, repo):
        self.task_repo = repo

    @staticmethod
    def finish_task(task: Task):
        task.state = 'finish'
        return task

    def list_all_tasks(self) -> List[Task]:
        all_task = self.task_repo.get_all_tasks()
        return sorted(all_task, key=lambda task: task.order_number)

    def list_active_tasks(self) -> List[Task]:
        active_tasks = self.task_repo.get_active_tasks()
        return sorted(active_tasks, key=lambda task: task.order_number)

    def create_task(self, name) -> Task:
        new_task = Task()
        new_task.task_name = name
        task_number = self.task_repo.get_all_task_count()
        new_task.order_number = task_number + 1
        self.task_repo.save_task(new_task)
