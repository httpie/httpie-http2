httpie-http2
============

Experimental HTTP/2 plugin for `HTTPie <http://httpie.org>`_.


Installation
------------

.. code-block:: bash

    # Transport plugins are supported only in the development version of HTTPie:
    $ pip install --upgrade https://github.com/jakubroztocil/httpie/tarball/master

    # This plugin is not on PyPi yet:
    $ pip install --upgrade https://github.com/jakubroztocil/httpie-http2/tarball/master


Usage
-----

.. code-block:: bash

    $ http https://host


Requirements
------------

* hyper_

.. _hyper: https://github.com/Lukasa/hyper
