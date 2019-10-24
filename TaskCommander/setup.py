# coding=utf-8
from setuptools import setup, find_packages

requirements = []

test_requirements = [
    'pytest'
]

setup(name='TaskCommander', version='0.1', package=find_packages, install_requires=requirements,
      test_requirements=test_requirements)
