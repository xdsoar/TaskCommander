from typing import List

from domain.task import Task
from texttable import Texttable


def create_task_list_view(tasks: List[Task]):
    table = Texttable()
    table.set_cols_align(['l', 'l'])
    table.set_cols_valign(['m', 'm'])
    table.add_row(["Task Number", "Task"])
    for task in tasks:
        table.add_row([task.order_number, task.task_name])
    return table.draw()
