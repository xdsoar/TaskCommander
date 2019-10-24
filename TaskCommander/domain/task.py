# coding=utf-8
import uuid


class Task:
    task_id: str

    task_name: str

    task_comment: str

    task_status: str

    def __init__(self, task_id=uuid.uuid1(), task_name='', task_comment='', task_status='active'):
        self.task_id = task_id
        self.task_name = task_name
        self.task_comment = task_comment
        self.task_status = task_status
