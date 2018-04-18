#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, Extension
except ImportError :
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow "
                      "the instructions for installing setuptools")

setup(
    name='objmatcher',
    url='https://github.com/jacobabello/objmatcher',
    version='0.02',
    author='Jacob Abello',
    author_email='abello.jacob@gmail.com',
    description='Match Generated Object and Return Similarity Score',
    packages=[
        'objmatcher'
    ],
    requires=[
        'numpy'
    ]
)