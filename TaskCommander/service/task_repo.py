# coding=utf-8
import json
from io import FileIO
from typing import List

from TaskCommander.domain.task import Task


class TaskRepo:
    task_file = "data.json"
    task_instance: List[Task] = None

    def __init__(self):
        if self.task_instance is None:
            self.__task_instance__init()

    def get_all_tasks(self) -> List[Task]:
        return self.task_instance

    def get_active_tasks(self) -> List[Task]:
        tasks = self.get_all_tasks()
        active_tasks = list(filter(lambda task: task.task_status == 'active', tasks))
        return active_tasks

    def save_task(self, task) -> Task:
        self.task_instance.append(task.__dict__)
        self.save()

    def save(self) -> Task:
        with open(self.task_file, 'r+') as file_stream:
            file_stream.seek(0)
            file_stream.truncate()
            file_stream.write(json.dumps(self.task_instance))
            file_stream.flush()

    def __task_instance__init(self):
        with open(self.task_file, 'r+') as file_stream:
            file_content = file_stream.read()
            if file_content is None or file_content == '':
                self.task_instance = []
            else:
                self.task_instance = json.loads(file_content)
