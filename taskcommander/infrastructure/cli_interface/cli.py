# coding=utf-8
import argparse
import sys

from taskcommander.service.task_repo import TaskRepo
from taskcommander.service.task_service import TaskService

task_service = TaskService(repo=TaskRepo())


def task_cli_output(tasks):
    print("----------------------------------------------------------------")
    for task in tasks:
        print("|    {task_name}     |".format(task_name=task.task_name))
    print("----------------------------------------------------------------")


def execute(command):
    print(command)
    if command.list:
        tasks = task_service.list_active_tasks()
        task_cli_output(tasks)
        return

    if command.add:
        task_service.create_task(command.add)


def prepare_parser(args):
    parser = argparse.ArgumentParser(description='hello world')
    parser.add_argument('--list', help='list all tasks', action='store_const', const='list')
    parser.add_argument('--add', help='add a task')

    # parser.add_argument('add')
    parsed_args = parser.parse_args(args)
    return parsed_args


if __name__ == '__main__':
    parsed_arg = prepare_parser(sys.argv)
    execute(parsed_arg)
