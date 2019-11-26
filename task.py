# coding=utf-8
import sys

from taskcommander.infrastructure.cli_interface import cli

if __name__ == '__main__':
    cli.prepare_parser(sys.argv)
