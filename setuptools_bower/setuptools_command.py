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

import setuptools


class BowerInstallCommand(setuptools.Command):
    """
    Setuptools command for running ```bower install```
    """

    description = "run bower"

    user_options = [
        ('force-latest', 'F', 'Force latest version on conflict'),
        ('production', 'p', 'Do not install project devDependencies'),
    ]

    boolean_options = ['production', 'force-latest']

    def initialize_options(self):
        """ Default values for options """
        self.force_latest = False
        self.production = False

    def finalize_options(self):
        """
        Finalize options

        TODO: .bowerrc issues can install in a different unknown place
        TODO: check existence of bower.json
        """
        pass

    def run(self):
        cmd = ['bower', 'install']
        if self.force_latest:
            cmd.append('-F')
        if self.production:
            cmd.append('-p')
        self.spawn(cmd)
