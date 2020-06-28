"""
Testing utilities

Created on Jun. 26, 2020

@author: Jonathan Gossage
"""

import os
from pathlib import Path
import sys
from types import ModuleType
from typing import Sequence, Union, Optional
import unittest


def gvTestController(envCheck: Union[Sequence[Union[Path, str]],
                                     Union[Path, str]]='lib.gvEnvChecks',
                     testPath: Optional[Union[Sequence[Union[Path, str]],
                                              Union[Path, str]]]=None,
                     caller: Optional[ModuleType]=None) -> int:
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

    def _ConstructSuite(mods: Union[Sequence[Optional[Union[Path, str]]],
                                    str]) -> unittest.TestSuite:
        _suite = unittest.TestSuite()
        if isinstance(mods, str):
            _suite.addTest(unittest.defaultTestLoader.
                           loadTestsFromName(mods))
        elif isinstance(mods, Sequence):
            for _m in mods:
                _suite.addTest.loadTestsFromName(_m)
        else:
            assert 'gvTest._ConstructSuite - Nothing to add to suite'
        return _suite

    def _reportErrors(_r: unittest.TestResult) -> str:
        errs = ''
        for e in _r.errors:
            errs += os.sep + f'Errors in {e[0]} - {e[1]}'
        for e in _r.failures:
            errs += os.sep + f'Failures in {e[0]} - {e[1]}'
        for e in _r.unexpectedSuccesses:
            errs += os.sep + f'Unexpected success in {e[0]} - {e[1]}'
        return errs

    def _gotContent(source: Optional[Union[Sequence[Optional[Union[Path,
                                                                   str]]],
                                           Union[Path, str],
                                           ModuleType]],
                    sequence: bool=False) -> bool:
        return source is not None and (sequence and
                                       (isinstance(source, Sequence) and
                                        len(source) > 0 and
                                        m is not None for m in source) or
                                       (isinstance(source, Path) or
                                        isinstance(source, str)) or
                                       isinstance(source, str))

    _gotTests = _gotContent(testPath,
                            sequence=True)
    _gotCaller = _gotContent(caller)
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
        _ts.addTest(unittest.defaultTestLoader.loadTestsFromName(caller))
    if envCheck is not None:
        # Run the prerequisite tests
        _ts.addTest(_ConstructSuite(envCheck))
    _tr: unittest.TestResult = _ts.run(unittest.TestResult())
    _rpt = 'Failure when running test prerequisites'
    if not _tr.wasSuccessful():
        if len(_tr.errors) > 0:
            raise ValueError(f'{_rpt}{os.sep}{_reportErrors(_tr)}')
        else:
            # We can't use an exception if one was raised during the test
            # If so, our exception will be lost
            print(f'{_rpt} - Success was {_tr.wasSuccessful()}'
                  ' and errors were'
                  f' {len(_tr.errors)}{os.sep}{_reportErrors(_tr)}')
            return _tr

    # Now we can run the tests themselves
    _ts = unittest.TestSuite()
    # First handle the module we are calling from
    if isinstance(testPath, Sequence):
        for mod in testPath:
            _ts.addTest(_ConstructSuite(testPath))
    else:
        _ts.addTest(_ConstructSuite(testPath))
    _tr = unittest.TestResult()
    _tr = _ts.run(_tr)  # Run the tests
    if not _tr.wasSuccessful() and\
            (len(_tr.errors) > 0 or len(_tr.failures) > 0):
        _rpt = 'Tests were not successful'
        print(_rpt + os.sep + _reportErrors(_tr),
              file=sys.stderr)
        return _tr
    return _tr
