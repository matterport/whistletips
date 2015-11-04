#!/usr/bin/env python -B

from setuptools import setup

version = '0.0.1'

setup(
    name='whistletips',
    version=version,
    description='AWS/boto3 helper library and reference tools',
    license='Unlicense',
    url='https://github.com/matterport/whistletips',
    packages=['whistletips'],
    setup_requires=[
        'flake8'
    ],
    install_requires=[
        'boto3'
    ],
    entry_points={
        'console_scripts': [
            'wt-lb = whistletips.wt_lb:main'
        ]
    }
)
