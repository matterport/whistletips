#!/usr/bin/env python

from setuptools import setup

version = '0.0.1'

setup(
    name='whistletips',
    version=version,
    author='Teran McKinney',
    author_email='sega01@go-beyond.org',
    description='AWS/boto3 helper library and reference tools',
    keywords=['boto3', 'aws'],
    license='Unlicense',
    url='https://github.com/matterport/whistletips',
    download_url='https://github.com/matterport/whistletips/tarball/' + version,
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
