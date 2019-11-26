# coding=utf-8
import unittest
from typing import List
from unittest import mock

from taskcommander.domain.task import Task
from taskcommander.service.task_service import TaskService


class TestTaskService(unittest.TestCase):
    mock_repo = mock.Mock()
    task_service = TaskService(repo=mock_repo)

    def test_get_task(self):
        # given
        task_list = [Task(task_name='a'), Task(task_name='b'), Task(task_name='c')]
        self.task_service.task_repo.get_all_tasks = mock.Mock(return_value=task_list)

        # when
        return_list = self.task_service.list_all_tasks()

        # then
        self.assertEqual(len(return_list), 3)
        self.assertEqual(return_list[0].task_name, 'a')
        self.assertEqual(return_list[1].task_name, 'b')
        self.assertEqual(return_list[2].task_name, 'c')

    def test_get_task_active(self):
        # given
        task_list = [Task(task_name='a'), Task(task_name='c')]
        self.task_service.task_repo.get_active_tasks = mock.Mock(return_value=task_list)

        # when
        return_list = self.task_service.list_active_tasks()

        # then
        self.assertEqual(len(return_list), 2)
        self.assertEqual(return_list[0].task_name, 'a')
        self.assertEqual(return_list[1].task_name, 'c')

    def test_save_task(self):
        class MemoryRepo:
            persistent_list: List[Task] = []

            def save_task(self, task):
                self.persistent_list.append(task)

            def get_all_tasks(self):
                return self.persistent_list

        repo = MemoryRepo()
        test_service = TaskService(repo=repo)
        test_service.create_task("test_task")

        saved_list = test_service.list_all_tasks()
        self.assertEqual(saved_list[0].task_name, 'test_task')
