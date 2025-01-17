#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

import restless


setup(
    name='restless',
    version=restless.VERSION,
    description='A lightweight REST miniframework for Python.',
    author='Daniel Lindsley',
    author_email='daniel@toastdriven.com',
    url='https://github.com/toastdriven/restless/',
    long_description=open('README.rst', 'r').read(),
    packages=[
        'restless',
    ],
    requires=[
    ],
    install_requires=[
    ],
    tests_require=[
        'mock',
        'tox',
    ],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Flask',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities'
    ],
)
