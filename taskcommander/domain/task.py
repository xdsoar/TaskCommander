# coding=utf-8
import uuid


class Task:
    task_id: str

    task_name: str

    task_comment: str

    task_status: str

    order_number: int

    def __init__(self, task_id=str(uuid.uuid1()), task_name='', task_comment='', task_status='active', order_number=0):
        self.task_id = task_id
        self.task_name = task_name
        self.task_comment = task_comment
        self.task_status = task_status
        self.order_number = order_number
