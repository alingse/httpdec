# coding=utf-8
# author@alingse
# 2016.12.30

from setuptools import setup, find_packages

from httpdec import __version__

version = '.'.join(map(str, __version__))

with open('README.rst') as f:
    readme = f.read()

setup(
    name='httpdec',
    version=version,
    description='a tool can decode http headers/cookies/...',
    long_description=readme,
    author='alingse',
    author_email='alingse@foxmail.com',
    url='https://github.com/alingse/httpdec',
    license='Apache 2.0',
    packages=find_packages(exclude=('tests')),
    install_requires=[
        'click',
        'python-dateutil'
    ],
    entry_points={
        'console_scripts': [
            'httpdec = httpdec.main:httpdec',
        ],
    }
)
