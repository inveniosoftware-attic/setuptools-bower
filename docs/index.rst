==================
 setuptools-bower
==================
.. currentmodule:: setuptools_bower

.. raw:: html

    <p style="height:22px;">
        <a href="https://travis-ci.org/inveniosoftware/setuptools-bower">
            <img src="https://travis-ci.org/inveniosoftware/setuptools-bower.png?branch=master"
                 alt="travis-ci badge"/></a>
        <a href="https://coveralls.io/r/inveniosoftware/setuptools-bower">
            <img src="https://coveralls.io/repos/inveniosoftware/setuptools-bower/badge.png?branch=master"
                 alt="coveralls.io badge"/></a>
    </p>

.. contents::
   :local:
   :backlinks: none

About
=====

setuptools-bower provides setuptools commands for integrating bower.

It provides additional setuptools commands ``build_npm``,
``build_bower``, and ``build_grunt``.  However, it does not install
``npm``, ``bower``, or ``grunt`` itself.

User's Guide
============

This part of the documentation will show you how to get started in using
setuptools-bower.

Installation
------------

Install setuptools-bower with ``pip`` ::

    pip install setuptools-bower

The development version can be downloaded from `its page at GitHub
<http://github.com/inveniosoftware/setuptools-bower>`_. ::

    git clone https://github.com/inveniosoftware/setuptools-bower.git
    cd setuptools-bower
    python setup.py develop
    ./run-tests.sh

Requirements
------------

**setuptools-bower** has the following dependencies:

- `setuptools <https://pypi.python.org/pypi/setuptools>`_
- `six <https://pypi.python.org/pypi/six>`_

setuptools-bower requires Python version 2.6, 2.7 or 3.3+

Usage
-----

After you install **setuptools-bower** you can run from within your Python
package:

.. code-block:: console

    python setup.py install_bower

This will run ``bower install`` in the directory and is thus expecting to
find a ``bower.json`` and respect any configuration in a ``.bowerrc``
file.

In your ``setup.cfg`` you may setup aliases to combine bower installation
with your normal install:

.. code-block:: ini

  [aliases]
  install_all = install_bower install

API Reference
=============

If you are looking for information on a specific function, class or
method, this part of the documentation is for you.

.. automodule:: setuptools_bower.setuptools_command
   :members:


Additional Notes
================

Notes on how to contribute, legal information and changelog are here for
the interested.

Contributing
------------

See <http://invenio-software.org/wiki/Development/Contributing> for now.


.. include:: ../CHANGES

License
-------

Copyright (C) 2013, 2014 CERN.

setuptools-bower is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

setuptools-bower is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with setuptools-bower; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

In applying this licence, CERN does not waive the privileges and immunities granted to it by virtue of its status as an Intergovernmental Organization or submit itself to any jurisdiction.

The full license text can be found in COPYING file.
