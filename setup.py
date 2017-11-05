"""This file contains setup information for socket echo server
assignment."""

from setuptools import setup

setup(
    name='Socket Echo Server',
    description='Contains setup for socket echo server assignment.',
    author='Nathan and Carson',
    author_email='carson.newton@outlook.com',
    package_dir={'': 'src'},
    py_modules=[],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox']}
)
