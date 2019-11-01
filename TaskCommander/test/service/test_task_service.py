# coding=utf-8
import unittest
from unittest import mock

from TaskCommander.domain.task import Task
from TaskCommander.service.task_repo import TaskRepo
from TaskCommander.service.task_service import TaskService


class TestTaskService(unittest.TestCase):
    task_service = TaskService()
    task_service.task_repo = TaskRepo()

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
        task_list = [Task(task_name='a'), Task(task_name='b', task_status='finish'), Task(task_name='c')]
        self.task_service.task_repo.get_all_tasks = mock.Mock(return_value=task_list)

        # when
        return_list = self.task_service.list_active_tasks()

        # then
        self.assertEqual(len(return_list), 2)
        self.assertEqual(return_list[0].task_name, 'a')
        self.assertEqual(return_list[1].task_name, 'c')
