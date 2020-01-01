# coding=utf-8
import os
import unittest

import taskcommander
from taskcommander.domain.task import Task
from taskcommander.service.task_repo import TaskRepo


class TestTaskRepo(unittest.TestCase):
    path = os.path.dirname(taskcommander.__file__)
    file_path = os.path.join(path, "test/resource/task.json")
    task_repo = TaskRepo(file_path)

    def setUp(self):
        with open(self.file_path, 'w') as file_stream:
            file_stream.seek(0)
            file_stream.truncate()
            file_stream.flush()
        self.task_repo = TaskRepo(self.file_path)

    def test_get_all_tasks(self):
        task_list = self.task_repo.get_all_tasks()
        self.assertEqual(len(task_list), 0)

    def test_add_task_to_file(self):
        task = Task(task_name='first task')
        self.task_repo.save_task(task)
        task_list = self.task_repo.get_active_tasks()
        self.assertEqual(len(task_list), 1)
        self.assertEqual(task_list[0].task_name, 'first task')

    def test_add_task_to_file_with_task_exists(self):
        task1 = Task(task_name='first task')
        self.task_repo.save_task(task1)
        self.task_repo = TaskRepo(self.file_path)
        task2 = Task(task_name='second task')
        self.task_repo.save_task(task2)
        task_list = self.task_repo.get_active_tasks()
        self.assertEqual(len(task_list), 2)
        self.assertEqual(task_list[0].task_name, 'first task')
        self.assertEqual(task_list[1].task_name, 'second task')
