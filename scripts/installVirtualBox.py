#!/usr/local/env python
# encoding: utf-8
"""
Steps:
    1. Setup Oracle repository in apt.
    2. Install VirtualBox from repository.
    3. Put current user in vboxusers group so that command line can be used.
    3. Perform non-user initialization.

installVirtualBox -- Install Oracle VirtualBox

installVirtualBox is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2020 organization_name. All rights reserved.

@license:    license

@contact:    user_email
"""

import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

__all__ = []
__version__ = 0.1
__date__ = '2020-06-17'
__updated__ = '2020-06-17'

DEBUG = 1
TESTRUN = 0
PROFILE = 0


class CLIError(Exception):
    """"Generic exception to raise and log different fatal errors."""
    def __init__(self,
                 msg):
        super()
        self._msg = f'E: {msg}'

    def __str__(self):
        return self._msg

    def __unicode__(self):
        return self._msg


class InstallVB():
    """Driver for the installation process"""
    def __init__(self,
                 verbose):
        self_verbose = verbose

    def __call__(self):
        return 0


def main(argv=None): # IGNORE:C0111
    """Command line options."""

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = f'v{__version__}'
    program_build_date = str(__updated__)
    program_version_message =\
        f'%%(prog)s {program_version} ({program_build_date})'
    program_license = f"""Install Oracle VirtualBox

  Created by Jonathan Gossage on { str(__date__)}.
  Copyright 2020 Global Village. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
"""

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license,
                                formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument('-v', '--verbose', dest='verbose', action='count',
                            help='set verbosity level [default: %(default)s]')
        parser.add_argument('-V', '--version', action='version',
                            version=program_version_message)

        # Process arguments
        args = parser.parse_args()

        return InstallVB(args.verbose)()
    except KeyboardInterrupt:
        # handle keyboard interrupt ###
        return 0
    except Exception as e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * ' '
        sys.stderr.write(program_name + ': ' + repr(e) + '\n')
        sys.stderr.write(indent + '  for help use --help')
        return 2


if __name__ == '__main__':
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'installVirtualBox_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open('profile_stats.txt', 'wb')
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())
