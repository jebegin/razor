import os
from setuptools import setup, find_packages

here = os.path.dirname(__file__)

setup(
    name='razor',
    version='0.0.1',
    author='Jacob Begin',
    author_email='jebeginmail@gmail.com',
    description='POC of vagrant python3',
    packages=find_packages(),
    # scripts=[os.path.join(here, "razor/foo.py")],
    install_requires=[
        'python-vagrant>=0.5.14',
        'rpyc>=3.3.0',
        'pytest>=3.0.6'
    ],
    include_package_data=True)
