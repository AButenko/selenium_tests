import os

import time
from setuptools import find_packages, setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def readme(fname='README'):
    """
    Utility function to read the README file.
    Used for the long_description.
    Args:
        fname: file name, usualy 'REAMDE'

    Returns:        text from 'README' file.

    """
    with open(os.path.join(os.path.dirname(__file__), fname)) as file:
        return file.read()

setup(
    name="framework",
    version="0.{}.{}".format(*time.localtime()),
    author="Anton Butenko",
    author_email="ant.butenko@gmail.com",
    description=("POC python framework."),
    license="BSD",
    packages=find_packages(),
    long_description=readme(),
    install_requires=[
        'selenium',
        'pytest',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)