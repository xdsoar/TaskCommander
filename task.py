# coding=utf-8
import sys

from TaskCommander.infrastructure.cli_interface import cli

if __name__ == '__main__':
    cli.prepare_parser(sys.argv)
