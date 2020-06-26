"""
Created on Apr. 19, 2020

@author: Jonathan Gossage

This code is based on code written by Fabio Zadrozny for his
`pvdev <https://www.pydev.org>`_ plugin for the Eclipse IDE.

This particular version is interim until the full ``StartApps`` package from
Global Village is available.

This module functions as a front end to the Python ``argparse`` module and makes
it unnecessary to fully program the argument parsing for each program
invocation. The argument parsing environment is dynamically constructed at
runtime instead of being statically compiled when the program is written.
Essentially, the program has become table driven so far as argument parsing is
concerned.
"""

import importlib
from pathlib import PurePath
import sys

from argparse import ArgumentParser, RawDescriptionHelpFormatter, Action


class handleVerbosity(Action):
    """
An argparse Action that limits the verbosity level to 3 for the verbose flag.
Note that making the verbosity level 3 also serves as a signal to run the
program in debugging mode.
    """
    def __init__(self,
                 option_strings,
                 dest,
                 **kwargs):
        super(option_strings,
              dest,
              kwargs)
        self._count = 0

    def __call__(self,
                 parser,
                 namespace,
                 values,
                 option_string=None):
        if ++self._count >= 3:
            if self._count == 3:
                print('Maximum permitted verbosity level is 3.'
                      ' Truncating level accordingly',
                      file=sys.stderr)
        else:
            setattr(namespace,
                    self.dest,
                    values)


class ArgumentDesc(object):
    """
    This class contains the internal description of an argument to be handled
    by ``argparse``.
    This class describes an individual entry in the list of possible arguments
    for a program. It will be used to generate **add_argument** function call
    that is used by the ``argparse`` parser to define the set of arguments that
    will be accepted for an invocation of the program that uses this software.

    No argument validation will be performed since the underlying ``argparse``
    parser will do the validation This means that there can be no conflict
    between this program and the argument parser. It ensures that the user will
    have no surprises. Note that the Python ``argparse`` documentation remains
    authoritative.

    :param str short_name:       This can either define the form of an optional
                                 short argument or it can contain the name of a
                                 mandatory positional argument. This argument
                                 must always be specified for a mandatory
                                 argument.
    :param str long_name:        This provides the form of the long name of an
                                 optional argument. At least one of
                                 ``short_name`` and ``long_name``` must be
                                 specified for an optional argument.
    :param str, function action: Specifies what should happen when this
                                 argument is encountered in a program. The
                                 argument may be a string that names the action
                                 to be taken or it may be a function that
                                 implements the action for situations where the
                                 standard  actions are not sufficient. The
                                 following standard actions can be specified:
                                 store      - Store the argument for use by the
                                              program. This is the default
                                              value                                              if this argument is not specified.
                                store_const - This is a constant, unchangeable
                                              argument that must be stored for
                                              use by the program. It stores the
                                              value specified by the ``const``
                                              optional argument.
                                store_true  - This argument and ``store_false``
                                              are special cases of
                                              ``store_const`` for boolean
                                              arguments.They will store True
                                              and False respectively.
                                store_false - See ``store_true``.
                                append      - Allows multiple instances of an
                                              optional argument. It creates a
                                              list and stores the value of each
                                              argument instance into the list
    """

    def __init__(self,
                 short_name=None,
                 long_name=None,
                 action=None,
                 args=None,
                 const=None,
                 default=None,
                 Type=None,
                 nargs=None,
                 choices=None,
                 required=None,
                 Help=None,
                 metavar=None,
                 dest=None):
        self._short_name = short_name
        self._long_name  = long_name
        self._action     = action
        self._nargs      = nargs
        self._const      = const
        self._default    = default
        self._type       = Type
        self._choices    = choices
        self._required   = required
        self._help       = Help
        self._metavar    = metavar
        self._dest       = dest

    @property
    def short_name(self):
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        self._short_name = value

    @property
    def long_name(self):
        return self._long_name

    @long_name.setter
    def long_name(self, value):
        self._long_name = value

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value

    @property
    def nargs(self):
        return self._nargs

    @nargs.setter
    def nargs(self, value):
        self._nargs = value

    @property
    def default(self):
        return self._default

    @default.setter
    def default(self, value):
        self._default = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def choices(self):
        return self._choices

    @choices.setter
    def choices(self, value):
        self._choices = value

    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value):
        self._required = value

    @property
    def help(self):
        return self._help

    @help.setter
    def help(self, value):
        self._help = value

    @property
    def metavar(self):
        return self._metavar

    @metavar.setter
    def metavar(self, value):
        self._metavar = value

    @property
    def dest(self):
        return self._dest

    @dest.setter
    def dest(self, value):
        self._dest = value


class Arguments(object):
    """Handles command line argument parsing"""

    def __init__(self,
                 program_version, updated):
        self._program_version = program_version
        self._updated = updated
        self._c = importlib.import_module('lib.configurationx')
        self._l = importlib.__import__('lib.gvLogging', fromlist=('Logging'))

    def Parse(self):
        if not self.get(self._c.noargs):
            return {}  # Command line processing not wanted
        # Construct messages used during command line argument parsing.
        #TODO: Fix accessing of build date
        # Build date is when the relevant module is successfully checked into
        # GitHub
        program_create_date = f'{self._c.cfg[self.datecr]}'
        program_build_date = str(self._updated)
        program_version_message = \
            '%%(prog)s {} {}'.format(self._program_version,
                                     program_build_date)
        program_shortdesc = __import__('__main__').__doc__.split('\n')[1]
        program_license = f"""{program_shortdesc}
Created by Jonathan Gossage on {program_create_date}.
Copyright © 2020 Jonathan Gossage All rights reserved.

Built on {program_build_date}.

Licensed under the Apache License 2.0
http://www.apache.org/licenses/LICENSE-2.0

Distributed on an "AS IS" basis without warranties
or conditions of any kind, either express or implied.

USAGE
"""
        # Setup argument parser
        parser = ArgumentParser(description=program_license,
                                prog=PurePath(sys.argv[0]).stem,
                                formatter_class=RawDescriptionHelpFormatter
                                )
        parser.add_argument('-v',
                            '--verbose',
                            dest='verbose',
                            action=handleVerbosity,
                            help='set verbosity level [default: 0]'
                            )
        parser.add_argument('-V',
                            '--version',
                            action='version',
                            version=program_version_message
                            )
#TODO: Add code to create more add_argument methods for items in configuration
# from configuration file

        # Process arguments
        return vars(parser.parse_args())
