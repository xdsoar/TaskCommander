# coding=utf-8
import json
import os
from typing import List, Dict

import pkg_resources
from taskcommander.domain.task import Task


class TaskRepo:
    task_instance: List[Task] = None

    def __init__(self, task_file="data.json"):
        resource_package = pkg_resources.get_distribution('taskcommander').location
        full_path = os.path.join(resource_package, task_file)
        self.task_file = full_path
        if self.task_instance is None:
            self.__task_instance__init()

    def get_all_tasks(self) -> List[Task]:
        return self.task_instance

    def get_active_tasks(self) -> List[Task]:
        tasks = self.get_all_tasks()
        active_tasks = list(filter(lambda task: task.task_status == 'active', tasks))
        return active_tasks

    def save_task(self, task) -> Task:
        self.task_instance.append(task)
        self.save()

    def save(self) -> Task:
        with open(self.task_file, 'r+') as file_stream:
            file_stream.seek(0)
            file_stream.truncate()
            file_stream.write(json.dumps([task.__dict__ for task in self.task_instance]))
            file_stream.flush()

    def __task_instance__init(self):
        with open(self.task_file, 'a+') as file_stream:
            file_content = file_stream.read()
            if file_content is None or file_content == '':
                self.task_instance = []
            else:
                task_dict_array: List[Dict] = json.loads(file_content)
                task_array = []
                for task_dict in task_dict_array:
                    task = Task()
                    task.task_id = task_dict.get("task_id")
                    task.task_name = task_dict.get("task_name")
                    task.task_comment = task_dict.get("task_comment")
                    task.task_status = task_dict.get("task_status")
                    task_array.append(task)
                self.task_instance = task_array
