====
TODO_PROJECT_NAME
====

TODO_COPYRIGHT_NOTICE

* Web site: TODO_PROJECT_WEB_SITE_URL
* Online documentation: TODO_PROJECT_ONLINE_DOCUMENTATION_URL
* Examples: TODO_PROJECT_ONLINE_DOCUMENTATION_URL/gallery/

* Notebooks: TODO_PROJECT_GITHUB_URL-notebooks
* Source code: TODO_PROJECT_GITHUB_URL
* Issue tracker: TODO_PROJECT_ISSUE_TRACKER_URL
* Pytest code coverage: TODO_PROJECT_ONLINE_DOCUMENTATION_URL/htmlcov/index.html
* TODO_PROJECT_NAME on PyPI: TODO_PROJECT_PYPI_URL
* TODO_PROJECT_NAME on Anaconda Cloud: https://anaconda.org/jdhp/TODO_PYTHON_PACKAGE_NAME


Description
===========

TODO_PROJECT_SHORT_DESC

Note:

    This project is still in beta stage, so the API is not finalized yet.


Dependencies
============

C.f. requirements.txt

.. _install:

Installation
============

Posix (Linux, MacOSX, WSL, ...)
-------------------------------

From the TODO_PROJECT_NAME source code::

    conda deactivate         # Only if you use Anaconda...
    python3 -m venv env
    source env/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    python3 setup.py develop


Windows
-------

From the TODO_PROJECT_NAME source code::

    conda deactivate         # Only if you use Anaconda...
    python3 -m venv env
    env\Scripts\activate.bat
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    python3 setup.py develop


Documentation
=============

* Online documentation: TODO_PROJECT_ONLINE_DOCUMENTATION_URL
* API documentation: TODO_PROJECT_ONLINE_API_DOCUMENTATION_URL


Example usage
=============

* Examples: TODO_PROJECT_ONLINE_DOCUMENTATION_URL/gallery/


Build and run the Python Docker image
=====================================

Build the docker image
----------------------

From the TODO_PROJECT_NAME source code::

    docker build -t TODO_PYTHON_PACKAGE_NAME:latest .

Run unit tests from the docker container
----------------------------------------

From the TODO_PROJECT_NAME source code::

    docker run TODO_PYTHON_PACKAGE_NAME pytest

Run an example from the docker container
----------------------------------------

From the TODO_PROJECT_NAME source code::

    docker run TODO_PYTHON_PACKAGE_NAME python3 /app/examples/hello.py


Bug reports
===========

To search for bugs or report them, please use the TODO_PROJECT_NAME Bug Tracker at:

    TODO_PROJECT_ISSUE_TRACKER_URL


License
=======

This project is provided under the terms and conditions of the `MIT License`_.


.. _MIT License: http://opensource.org/licenses/MIT
.. _command prompt: https://en.wikipedia.org/wiki/Cmd.exe
