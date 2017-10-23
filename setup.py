"""This file contains setup information for socket echo server
assignment."""

from setuptools import setup

setup(
    name='Data-Structures',
    description='Contains setup for Data-Structures modules.',
    author='Chelsea and Carson',
    author_email='carson.newton@outlook.com, chelseadole@gmail.com',
    package_dir={'': 'src'},
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov']}
)
