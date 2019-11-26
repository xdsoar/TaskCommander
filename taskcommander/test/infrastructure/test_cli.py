# coding=utf-8
import unittest

from infrastructure.cli_interface import cli


class TestCli(unittest.TestCase):

    def test_Prepare_parser(self):
        args = ['--list']
        parsed_args = cli.prepare_parser(args)
        self.assertIsNotNone(parsed_args.list)
