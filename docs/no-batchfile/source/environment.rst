########################################
*Global Village* Development Environment
########################################

This section describes the *Global Village* software development environment and
it's components. Eventually, the whole process of generating and maintaining the
*Global Village* software development environment will be automated. These notes
will help develop the automated environment as well as support the interim
manual environment.

***********
Major Tools
***********

Operating System
================

The *Global Village* is platforrm neutral and the development environment can be
installed on any supported platform. The implication of a supported platform is
that we know how to create the platform and can automate this process.

Linux
-----

Ubuntu
^^^^^^

Disk Layout
"""""""""""

The following principles should be observed when deciding on a disk layout:

* The operating system should be cleanly disassociated from the user's
  environment. This helps to make it easy to reinstall the operating system with
  minimal effort and preserves the user's data accross operating system
  reinstallations.
* Configuration data for tools is often stored in the user's home directory.
  Where possible it should not be placed in the home directory as it is rebuilt
  when the operating system is reinstalled. Tricks like symbolic links can help
  here. Where possible, the tools themselves should not be installed on the
  operating system so that they will not need re-installation when the operating
  system is reinstalled. Many tools offer this option at installation time. On
  some Linux systems, the location of the `/usr/local/bin directory` can be
  placed outside of the installation environment thus preserving local tools
  when an operating system reinstallation is performed.

Windows
-------

The nature of a software development environment that supports Windows has not
yet been determined. It will follow, as closely as possible, the development
environment for Linux.

Development Tools
=================

These are the principal tools used by the *Global Village* organization. They
must be installed into the operating system environment.

Eclipse
-------

This is a cross-platform IDE that supports software development. It can be
installed from the `Eclipse Download`_ site.

PyDev
^^^^^

This is a plugin for Eclipse that supports Python development. It can be
installed via the `Eclipse Marketplace`_. It is not usable outside of Eclipse.

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

This component can be installed via the `Eclipse Marketplace`_ It is not usable
outside of Eclipse.

Python
------

This is the primary programming language used by the *Global Village* for
software development. It can be installed from the `Python`_ downloads site.

Sphinx
------

This is the tool used for creating documentation in the *Global Village*
environment. it is based on Python and can be installed from within PyDev using
the following pip command, getting the software from the
`Python Package Index`_ site.

`pip install sphinx`.

Git
---

This tool manages all changes to the software source text. The installation
process varies, depending on the operating system used for the development
environment.
