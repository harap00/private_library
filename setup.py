from setuptools import setup, find_packages

install_requires = [
    'yapf',
    'isort',
    'autopep8'
]

setup(
    name='max_fmt',
    version='0.1',
    packages=find_packages()
)
