# coding=utf-8
import os
import unittest

import taskcommander
from taskcommander.service.task_repo import TaskRepo


class TestTaskRepo(unittest.TestCase):
    path = os.path.dirname(taskcommander.__file__)
    task_repo = TaskRepo(os.path.join(path, "test/resource/task.json"))

    def test_get_all_tasks(self):
        task_list = self.task_repo.get_all_tasks()
        self.assertEqual(len(task_list), 0)
