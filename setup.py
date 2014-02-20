# -*- coding: utf-8 -*-
##
## This file is part of setuptools-bower
## Copyright (C) 2013 CERN.
##
## setuptools-bower is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## setuptools-bower is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with setuptools-bower; if not, write to the Free Software Foundation,
## Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
##
## In applying this licence, CERN does not waive the privileges and immunities
## granted to it by virtue of its status as an Intergovernmental Organization
## or submit itself to any jurisdiction.

from setuptools import setup

setup(
    name='setuptools-bower',
    version='0.1',
    url='http://github.com/inveniosoftware/setuptools-bower/',
    license='GPLv2',
    author='Invenio collaboration',
    author_email='info@invenio-software.org',
    description='Setuptools commands for integrating bower',
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
    ],
    entry_points={
        "distutils.commands": [
            "build_bower = setuptools_bower.setuptools_command:BowerBuildCommand",
            "build_grunt = setuptools_bower.setuptools_command:GruntBuildCommand",
            "build_npm = setuptools_bower.setuptools_command:NPMBuildCommand",
        ]
    },
    test_suite='nose.collector',
    tests_require=['nose', ],
)
