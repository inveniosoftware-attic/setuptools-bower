==================
 setuptools-bower
==================

.. image:: https://travis-ci.org/inveniosoftware/setuptools-bower.png?branch=master
    :target: https://travis-ci.org/inveniosoftware/setuptools-bower
.. image:: https://coveralls.io/repos/inveniosoftware/setuptools-bower/badge.png?branch=master
    :target: https://coveralls.io/r/inveniosoftware/setuptools-bower
.. image:: https://pypip.in/v/setuptools-bower/badge.png
   :target: https://pypi.python.org/pypi/setuptools-bower/
.. image:: https://pypip.in/d/setuptools-bower/badge.png
   :target: https://pypi.python.org/pypi/setuptools-bower/

About
=====
setuptools-bower provides setuptools commands for integrating bower.

Usage
=====
setuptools-bower is on PyPI so all you need is: ::

    pip install setuptools-bower

Then from within your Python package, you can now run::

    python setup.py install_bower

This will run ```bower install``` in the directory and is thus expecting to find a ```bower.json``` and respect any configuration in a ```.bowerrc``` file.

In your ```setup.cfg``` you may setup aliases to combine bower installation with your normal install::

  [aliases]
  install_all = install_bower install

Documentation
=============
Documentation is readable at http://setuptools-bower.readthedocs.org or can be build using Sphinx: ::

    git submodule init
    git submodule update
    pip install Sphinx
    python setup.py build_sphinx

Testing
=======
Running the test suite is as simple as: ::

    python setup.py test

or, to also show test coverage: ::

    ./run-tests.sh
