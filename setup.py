#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

from setuptools import setup

with open('README.md') as f:
    desc = f.read()

setup(
    name='niacin',
    version='0.1.0',
    packages=[
        'niacin'
    ],
    package_data={
        'niacin': ['data/*']
    },
    install_requires=[
        'nltk',
        'regex',
        'scipy',
    ],
    long_description=desc,
    long_description_content_type="text/markdown",
    tests_require=[
        'pytest',
        'pytest-cov'
    ]
)
