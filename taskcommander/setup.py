# coding=utf-8
from setuptools import setup, find_packages

requirements = [
    'texttable'
]

test_requirements = [
    'pytest', 'pytest-cov'
]

extras = {
    'test': test_requirements
}

setup(name='taskcommander', version='0.11', package=find_packages, install_requires=requirements,
      test_requirements=test_requirements, extras_require=extras)
