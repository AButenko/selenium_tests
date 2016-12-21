import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as file:
        readme = file.read()
    return readme

setup(
    name="framework",
    version="0.0.1",
    author="Anton Butenko",
    author_email="ant.butenko@gmail.com",
    description=("POC python framework."),
    license="BSD",
    packages=['framework'],
    long_description=read('README'),
)