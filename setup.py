# -*- coding: utf-8 -*-
##
## This file is part of setuptools-bower
## Copyright (C) 2013, 2014 CERN.
##
## setuptools-bower is free software; you can redistribute it and/or
## modify it under the terms of the Revised BSD License; see LICENSE
## file for more details.

import os
import re

from setuptools import setup

# Get the version string.  Cannot be done with import!
with open(os.path.join('setuptools_bower', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

setup(
    name='setuptools-bower',
    version=version,
    url='http://github.com/inveniosoftware/setuptools-bower/',
    license='BSD',
    author='Invenio collaboration',
    author_email='info@invenio-software.org',
    description='Setuptools commands for integrating bower.',
    long_description=open('README.rst').read(),
    packages=['setuptools_bower', ],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'setuptools>=2.0',
        'six',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Setuptools Plugin',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 5 - Production/Stable',
    ],
    entry_points={
        "distutils.commands": [
            "build_bower = setuptools_bower.setuptools_command:BowerBuildCommand",
            "build_grunt = setuptools_bower.setuptools_command:GruntBuildCommand",
            "build_npm = setuptools_bower.setuptools_command:NPMBuildCommand",
        ]
    },
    test_suite='nose.collector',
    tests_require=['nose', 'pep8', 'pep257'],
)
