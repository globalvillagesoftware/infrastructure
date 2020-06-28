#!/usr/bin/env python
"""
Capture Linux platform dependent information

Created on May 27, 2020

@author: Jonathan Gossage

This module is designed to run at boot time and it extracts a bunch of platform
dependent information and makes it available to other script modules via
platform environment variables.
"""

import os
import re
from typing import Dict, Any, List, Match

import lib.environmentAccess as ea
from lib.environmentAccess import gvEnvironmentError


def PlatformWorker() -> None:
    import platform  #pylint: disable=import-outside-toplevel

    # This ensures that all supported environment variables get a default value
    # and become defined in os.environ
    un: Dict[str, Any]\
        = {ea.GVSYSTEM: None, ea.GVNODE: None, ea.GVDISTRORELEASE: None,
           ea.gvDistributorName: None, ea.gvDistroDesc: None,
           ea.gvDistroCodename: None, ea.gvOSRelease: None,
           ea.gvOSReleaseDesc: None, ea.gvMachine: None, ea.gvProcessor: None,
           ea.gvGnu: None, ea.gvOSName: None}
    s: str = platform.system()
    try:
        if s != 'linux':
            raise ea.gvEnvironmentError(
                f'Linux is the only supported platform - {s} detected')
        un[ea.GVSYSTEM] = s
        un[ea.GVNODE] = platform.node()
        un[ea.gvMachine] = platform.machine()
        un[ea.gvProcessor] = platform.processor()
        # Isolate the OS release number and the full description
        r: str = platform.release()
        un[ea.gvOSRelease] = None
        if s == 'linux':
            m: Match = re.match(r'((\d+\.\d+)(\.\d+)?(-\d+)?)',
                                r,
                                re.VERBOSE)
            if m is not None:
                print(f'Matching release groups - {m.span(1)/m.group(1)}')
                un[ea.gvOSRelease] = m.group(1)
                un[ea.gvOSReleaseDesc] = m.group(0)
            else:
                raise ea.gvEnvironmentError(
                    f'Linux OS release syntax invalid in {r}')
    finally:
        os.environ.update(un)


def LsbWorker() -> None:
    import subprocess  #pylint: disable=import-outside-toplevel
    import sys  #pylint: disable=import-outside-toplevel

    le: Dict[str, Any] = {}
    if os.environ[ea.GVSYSTEM] != 'linux':
        return  # lsb_release only supported on Linux
    try:
        ret = subprocess.run(['lsb_release', '-a'], text=True,
                             capture_output=True, check=True)
        ret.check_returncode()
    except subprocess.CalledProcessError as ex:
        print(ex, file=sys.stderr, flush=True)
        raise  # Unable to successfully run command
    out: List[str] = ret.stdout.splitlines()    # get the output from
                                                # lsb_release as a list
                                    # of lines
    # These are the keys in the text produced by the lsb_rlease command. They
    # identify the contents of the  rest of the line.
    keys: List[str]\
        = ['LSB Version', 'Distributor ID', 'Description',
           'Release', 'Codename']
    for l in out:  # loop through each line of the command output
        # First we want to isolate the line key so we can test it
        # The key is basically alphabetic but it may contain any number
        # of embedded spaces, The key is terminated by a colon.
        rexfm =\
r"""
# The regular expression that provides the rules for the basic parsing of a
# lsb_release output line. This expression makes use of lookahead to verify
# that the expected sequence of characters exists.
 (  # The start of the group that will contain the line key
    # The key starts with a upper case alphabetic followed by an alphabetic or
    # by an embedded space.
    [A-Z](?=[A-Za-z]|\s[A-Za-z]|:)
    # It is followed by a sequence of alphabetic characters that may contain
    # embedded spaces
    [A-Za-z](?=[A-Za-z]|\s[A-Za-z]\:)|\s(?=[A-Za-z])+
 )  # End of group containing line key
# The rest of the string is captured in a group whose analysis will depend on
# the type of key encountered.
:\s+(.+)
"""
        m: Match = re.fullmatch(rexfm,
                                l,
                                re.VERBOSE)
        if m.groups(1) == keys[0]:    # Ignore the LSB Version key
            pass
        elif m.groups(1) == keys[2]:    # We have a distribution id
            pass
        elif m.groups(1) == keys[3]:    # we have a distribution description
            pass
        elif m.groups(1) == keys[4]:    # We have an operating system release
                                        # description
            pass
        elif m.groups(1) == keys[5]:    # we have a Linux distribution code
                                        # name:
            if not isinstance(m.group(1), str):
                raise(gvEnvironmentError('Syntax error in key describing'
                                         ' lsb_release text output- got'
                                         f' {m.group(1)}'))
            elif isinstance(m.group(2), str):
                le[m.group(1)] = m.group(2)
            else:
                raise(gvEnvironmentError('Syntax error in value of'
                                         ' lsb_release text output'
                                         f' - got {m.group(2)}'))
        else:                           # Ignore unrecognized keys
            pass

        # Now update os.environ
        os.environ.update(le)


# Invoke the support
PlatformWorker()
LsbWorker()
