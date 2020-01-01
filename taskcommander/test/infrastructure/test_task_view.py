from unittest import TestCase

from domain.task import Task
from infrastructure.cli_interface.task_view import create_task_list_view


class TestTaskView(TestCase):

    def test_create_task_list_view(self):
        # given
        task1 = Task(task_name='task1')
        task1.order_number = 1
        task2 = Task(task_name='task2')
        task2.order_number = 2
        task3 = Task(task_name='task3')
        task3.order_number = 3
        # when
        output_view = create_task_list_view([task1, task2, task3])

        # then
        lines = output_view.split("\n")
        self.assertEqual(lines[3], '| 1           | task1 |')
        self.assertEqual(lines[5], '| 2           | task2 |')
