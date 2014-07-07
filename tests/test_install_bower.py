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

import os
import shutil
import tempfile
from unittest import TestCase

from setuptools.dist import Distribution
from setuptools_bower.setuptools_command import BowerBuildCommand, \
    NPMBuildCommand, GruntBuildCommand


SETUP_ATTRS = {
    'name': 'bower_install_test',
    'version': '0.0',
}


SETUP_PY = """\
from setuptools import setup

setup(**%r)
""" % SETUP_ATTRS


BOWER_JSON = """
{
  "name": "bower_install_test",
  "version": "0.0.0",
  "dependencies": {
    "jquery": "~1.10.2"
  }
}
"""

BOWERRC = """
{
    "directory": "bower_components"
}
"""

PACKAGES_JSON = """
{
  "name": "npm_install_test",
  "version": "0.0.0",
  "dependencies": {
    "grunt": "*",
    "grunt-cli": "*"
  }
}
"""

GRUNTFILE_JS = """
module.exports = function(grunt) {
    grunt.registerTask('build', 'Setup test', function () {
       if (grunt.option('path') === undefined) {
            return true
       } else {
            return grunt.option('path') == 'test'
       }
    });
}
"""


class TestBowerBuildCommand(TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

        for filename, content in [('setup.py', SETUP_PY),
                                  ('bower.json', BOWER_JSON),
                                  ('.bowerrc', BOWERRC),
                                  ('package.json', PACKAGES_JSON),
                                  ('Gruntfile.js', GRUNTFILE_JS),
                                  ]:
            f = open(os.path.join(self.temp_dir, filename), 'w')
            f.write(content)
            f.close()

        self.old_cwd = os.getcwd()
        os.chdir(self.temp_dir)

    def tearDown(self):
        os.chdir(self.old_cwd)
        shutil.rmtree(self.temp_dir)

    def test_bower_install(self):
        """Test bower install command."""
        assert not os.path.exists(
            os.path.join(self.temp_dir, 'bower_components')
        )

        assert not os.path.exists(
            os.path.join(self.temp_dir, 'node_modules')
        )

        dist = Distribution(SETUP_ATTRS)
        dist.script_name = 'setup.py'

        cmd = NPMBuildCommand(dist)
        cmd.ensure_finalized()
        cmd.run()

        assert os.path.exists(os.path.join(self.temp_dir, 'node_modules'))

        cmd = BowerBuildCommand(dist)
        cmd.ensure_finalized()
        cmd.run()

        assert os.path.exists(os.path.join(self.temp_dir, 'bower_components'))

        cmd.force_latest = True
        cmd.run()

        cmd.production = True
        cmd.run()

        cmd = GruntBuildCommand(dist)
        cmd.ensure_finalized()
        cmd.run()

        cmd.path = 'test'
        cmd.run()
