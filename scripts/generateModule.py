#!/usr/local/bin/python3.8
# encoding: utf-8
"""
Script to generate **Python** module from a *Jinja2* template.

Optionally, it may be used to generate source code or to generate bytecode.
The script can produce a source module or it can load templates that extend
other templates. This can be controlled on an individual template basis.
The script defaults to generating bytecode.

.. only:: development_administrator

    @author:     Jonathan Gossage
    
    @copyright:  2020 Global Village. All rights reserved.
    
    @license:    Apache2
    
    @contact:    jgossage@gmail.com
    @deffield    updated: Updated
"""

import sys
import os
from importlib import import_module
from pathlib import Path
from typing import Sequence, Optional, Any, Callable, MutableMapping

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

import jinja2



__all__ = []
__version__: str = '0.1'
__date__ = '2020-07-17'
__updated__ = '2020-07-17'

DEBUG = 0
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    """Generic exception to raise and log different fatal errors."""
    def __init__(self: 'CLIError',
                  msg: str):
        super(self)
        self.msg = 'E: %s' % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def run(args: Optional[Sequence[str]]=None) -> int:
    """Runs the actual script"""
    # Setup the template loader
    # Loop processing the requested template containers
    for n in args.name:
        tc = TemplateContainer(n)
        tc.FindTemplate()
        tc.GlobalVariables()
        tc.CompileTemplate()
        tc.RenderTemplate()
    return 0

def main(argv:Optional[str]=None) -> int: # IGNORE:C0111

    """Command line options."""

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = Path(sys.argv[0]).stem
    program_version = f'v{__version__}'
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split('\n')[1]
    program_license = f"""{program_shortdesc}

  Created by Jonathan Gossage on {str(__date__)}.
  Copyright 2020 Global Village. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an 'AS IS' basis without warranties
  or conditions of any kind, either express or implied.

USAGE
"""

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license,
                                formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument('-v',
                            '--verbose',
                            dest='verbose',
                            action='count',
                            help='set verbosity level [default: %(default)s]')
        parser.add_argument('-V',
                            '--version',
                            action='version',
                            version=program_version_message)
        parser.add_argument('-t',
                            '--templates',
                            dest='templates',
                            default='./templates',
                            help='directory containing Jinja2 templates')
        parser.add_argument('-b',
                            '--bytecode',
                            dest='bytecode',
                            default='./__pycache__',
                            help='bytecode destination-'
                            ' If None, source code will be generated in ..')
        parser.add_argument('name',
                            dest='name',
                            nargs='*',
                            help='Name(s) of Jinja2 template container(s)'
                                 ' to be handled')

        # Process arguments
        args = vars(parser.parse_args())

        run(args)
        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception as e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * ' '
        sys.stderr.write(f'{program_name}: {repr(e)}\n')
        sys.stderr.write(f'{indent}  for help use --help')
        return 2

if __name__ == '__main__':
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'scripts.generateModule_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open('profile_stats.txt', 'wb')
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())