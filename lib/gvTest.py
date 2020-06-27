"""
Testing utilities

Created on Jun. 26, 2020

@author: Jonathan Gossage
"""

import os
from pathlib import Path
import sys
from typing import Sequence, Union, Optional
import unittest


def gvTestController(envCheck: Union[Sequence[Union[Path, str]],
                                     Union[Path, str]]=Path('lib/gvEnvChecks'),
                     testPath: Optional[Union[Sequence[Union[Path, str]],
                                              Union[Path, str]]]=None,
                     caller: Union[Path, str]='') -> int:
    """
    Standard *Global Village* test controller

    This function uses and supports the standard **Python** unit testing
    environment as supplied in the `unittest` module.

    The standard *Global Village* unit testing environment assumes that certain
    capabilities do not need mocking. Instead, when running unit tests, a set
    of tests is run as a sanity check on the standard environment before the
    tests of interest are run. This supports the assumption that all tests can
    assume the presence of certain verified functionality and use this
    functionality in unit tests without having to use mock objects. This
    functionality includes logging and the discovery and setting of various
    platform dependent variables that are used throughout the *Global Village*
    environment.

    If the environment is specified, the set of `TestCase` classes in the test
    environment test prerequisites module is run and they must succeed before
    the requested set of tests can run.

    This is done by collecting the prerequisite set of tests into a `unittest`
    test suite and running this suite first. These prerequisites are all
    contained in a single module. The module containing these tests is
    specified by the`envCheck` argument. This is a keyword argument
    that defaults to the standard test set. If any test fails, the results are
    presented to the user and the actual tests are not run.

    If the prerequisites run successfully, the tests in the module that invokes
    this functionality are collected into a suite, followed by the tests from
    any modules specified in the `test` argument, then the actual test suite is
    run and the results are presented to the user.
    """

    print(f'Entered gvTestController: name is {__name__}')

    def _ConstructSuite(mods: Union[Sequence[Optional[Union[Path, str]]],
                                    Union[Path, str]]) -> unittest.TestSuite:
        _suite = unittest.TestSuite()
        _suite.addTest(unittest.defaultTestLoader.
                       loadTestsFromModule(mods if isinstance(mods,
                                                              str)
                                           else mods.name))
        return _suite

    def reportErrors(_r: unittest.TestResult) -> str:
        errs = ''
        for e in _r.errors:
            errs += os.sep + f'Errors in {e[0]} - {e(1)}'
        for e in _r.failures:
            errs += os.sep + f'Failures in {e[0]} - {e[1]}'
        for e in _r.unexpectedSuccesses:
            errs += os.sep + f'Unexpected success in {e[0]} - {e[1]}'
        return errs

    def gotContent(source: Optional[Union[Sequence[Optional[Union[Path,
                                                                  str]],
                                          Path, str]]],
                   sequence: bool=False) -> bool:
        return source is not None and (sequence and
                                       (isinstance(source, Sequence) and
                                        len(source) > 0 and
                                        m is not None for m in source) or
                                       isinstance(source, Path) or
                                       (isinstance(source, str) and
                                        source != ''))

    _gotTests = gotContent(testPath,
                           sequence=True)
    _gotCaller = gotContent(caller)
    if not _gotTests and not _gotCaller:
        raise ValueError('gvTest - No tests supplied. nothing to do')
    if not isinstance(envCheck, Sequence) and\
       not isinstance(envCheck, Path) and\
       not isinstance(envCheck, str):
        raise ValueError('gvTest - invalid type for prerequisites list'
                         f' - {repr(envCheck)}')
    _ts = unittest.TestSuite()
    # Adding ourselves to the list of modules containing test cases
    if (caller is not None) and _gotCaller:
        _ts.addTest(caller)
    if envCheck is not None:
        _ts.addTest(_ConstructSuite(envCheck))
    _tr: unittest.TestResult = _ts.run()  # Run the prerequisite tests
    if not _tr.wasSuccessful():
        _rpt = 'Failure when running test prerequisites'
        raise ValueError(f'{reportErrors(_rpt)}')

    # Now we can run the tests themselves
    _ts = unittest.TestSuite()
    # First handle the module we are calling from
    print(f'Module name is {__name__}')
    for mod in testPath:
        _ts.addTest(_ConstructSuite(mod))
    _tr = _ts.run()  # Run the tests
    if not _tr.wasSuccessful():
        _rpt = 'Tests were not successful'
        print(_rpt + reportErrors(_tr),
              file=sys.stderr)
        return 1
    return 0
