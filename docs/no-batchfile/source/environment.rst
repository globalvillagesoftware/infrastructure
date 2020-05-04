######################################
Global Village Development Environment
######################################

This section describes the Global Village software development environment and
it's components.

.. ref _software-prerequisites:

***********
Major Tools
***********

Operating System
================

Linux
-----

Ubuntu
^^^^^^

Disk Layout
"""""""""""

The following principles should be observed when deciding on a disk layout:

Windows
-------

The nature of an sofyware development environment that supports Windows has not
yet been determined. It will follow, as closely as possible, the development
environment for Linux.

Development Tools
=================

These are the principal tools used by the *Global Village* organization. They
must be installed into the operating system environment.

Eclipse
-------

This is a cross-platform IDE that supports software development. It can be
installed from the
`Eclipse download site <https://www.eclipse.org/downloads/>`_.

PyDev
^^^^^

This is a plugin for Eclipse that supports Python development. It can be
installed via the `Eclipse Marketplace <https://marketplace.eclipse.org/>`_. It
is not usable outside of Eclipse.

LiclipseText
^^^^^^^^^^^^

This is a plugin for Eclipse that is a text editing tool that supports many
formats including:

* RST |br| 
  The language used for Sphinx documentation source.
* HTML |br| 
  The language that defines the content on most websites and that can be
  displayed by most browsers.
* CSS |br| 
  The language that is used to define the styling rules for an HTML display.

This component can be installed via the
`Eclipse Marketplace <https://marketplace.eclipse.org/>`_. It is not usable
outside of Eclipse.

Python
------

This is the primary programming language used by the *Global Village* for
software development. It can be installed from the
`Python downloads site <https://www.python.org/downloads/>`_.

Sphinx
------

This is the tool used for creating documentation in the *Global Village*
environment. it is based on Python and can be installed from within PyDev via
the following pip command from the
`Python Package Index site <https://pypi.org/>`_.

`pip <https://pypi.org/project/pip/>`_ `install sphinx`.

Git
---

This tool manages all changes to the software source text. The installation
process varies, depending on the operating system used for the development
environment.
