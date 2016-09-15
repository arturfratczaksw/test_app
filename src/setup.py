import sys
import setuptools
from setuptools.command.test import test as TestCommand

import smoothwall

setuptools.setup(
    name='smoothwall',
    version=smoothwall.__version__,
    author_email='artur.fratczak@smoothwall.net',
    include_package_data=True,
    packages=setuptools.find_packages(),
    scripts=['scripts/run_whoami']
)