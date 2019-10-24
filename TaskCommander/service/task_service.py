# coding=utf-8
from typing import List

from TaskCommander.domain.task import Task
from TaskCommander.service.task_repo import TaskRepo


class TaskService:
    task_repo: TaskRepo

    @staticmethod
    def finish_task(task: Task):
        task.state = 'finish'
        return task

    def list_all_tasks(self) -> List[Task]:
        return self.task_repo.get_all_tasks()

    def list_active_tasks(self) -> List[Task]:
        return self.task_repo.get_active_tasks()

    def create_task(self) -> Task:
        new_task = Task()
        self.task_repo.save_task(new_task)
