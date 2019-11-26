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
        return self.task_repo.get_all_tasks()

    def list_active_tasks(self) -> List[Task]:
        return self.task_repo.get_active_tasks()

    def create_task(self, name) -> Task:
        new_task = Task()
        new_task.task_name = name
        self.task_repo.save_task(new_task)
