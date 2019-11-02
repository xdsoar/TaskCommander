# coding=utf-8
import json
from io import FileIO
from typing import List

from TaskCommander.domain.task import Task


class TaskRepo:
    task_file = "data.json"
    file_io: FileIO
    task_instance: List[Task]

    def get_all_tasks(self) -> List[Task]:
        if self.task_instance is None:
            self.__task_instance__init(self.task_file)
        return self.task_instance

    def get_active_tasks(self) -> List[Task]:
        tasks = self.get_all_tasks()
        active_tasks = list(filter(lambda task: task.task_status == 'active', tasks))
        return active_tasks

    def save_task(self, task) -> Task:
        self.task_instance.append(task)
        self.save()

    def save(self) -> Task:
        self.file_io.write(json.dumps(self.task_instance))
        self.file_io.flush()

    def __task_instance__init(self):
        self.file_io = open(self.task_file, 'w')
        self.task_instance = json.loads(self.file_io.read())
