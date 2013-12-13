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