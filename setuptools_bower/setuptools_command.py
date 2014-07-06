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

"""Custom setuptools commands implementation."""

import setuptools


class BowerBuildCommand(setuptools.Command):

    """Setuptools command for running ``bower <command>``."""

    description = "run bower commands."

    user_options = [
        ('bower-command=', 'c',
         'Bower command to run. Defaults to \'install\'.'),
        ('force-latest', 'F', 'Force latest version on conflict.'),
        ('production', 'p', 'Do not install project devDependencies.'),
    ]

    boolean_options = ['production', 'force-latest']

    def initialize_options(self):
        """Set default values for options."""
        self.force_latest = False
        self.production = False
        self.bower_command = 'install'

    def finalize_options(self):
        """Finalize options."""
        pass

    def run(self):
        """Execute ``bower`` command."""
        cmd = ['bower', self.bower_command]
        if self.force_latest:
            cmd.append('-F')
        if self.production:
            cmd.append('-p')
        self.spawn(cmd)


class GruntBuildCommand(setuptools.Command):

    """Setuptools command for running ``grunt <command>``."""

    description = "run grunt commands."

    user_options = [
        ('grunt-command=', 'c',
         'Grunt command to run. Defaults to \'build\'.'),
        #('force-latest', 'F', 'Force latest version on conflict.'),
        ('path=', 'p', 'Path.'),
    ]

    def initialize_options(self):
        """Set default values for options."""
        self.path = None
        self.grunt_command = 'build'

    def finalize_options(self):
        """Finalize options."""
        pass

    def run(self):
        """Execute ``grunt`` command."""
        cmd = ['grunt']
        if self.grunt_command:
            cmd.append(self.grunt_command)
        if self.path:
            cmd.append('--path=%s' % self.path)
        self.spawn(cmd)


class NPMBuildCommand(setuptools.Command):

    """Setuptools command for running ``npm <command>``."""

    description = "run NPM commands."

    user_options = [
        ('npm-command=', 'c',
         'NPM command to run. Defaults to \'install\'.'),
    ]

    def initialize_options(self):
        """Set default values for options."""
        self.npm_command = 'install'

    def finalize_options(self):
        """Finalize options."""
        pass

    def run(self):
        """Execute ``npm`` command."""
        cmd = ['npm', self.npm_command]
        self.spawn(cmd)
