"""
Check initial module design

This test is used during the conceptual stages of application development to
ensure that all classes embedded in a *Python* module assert that they are not
implemented. This check is done by verifying that each class sends a warning
level error message to the gvLogging system. NotImplemented exceptions are not
used because a module may a mixture of implemented and non-implemented classes
during development.

Created on Jun. 20, 2020

@author: jgossage
"""
import unittest
import os

import gvMultiprocessing


class Test(unittest.TestCase):

    def testClassesNotImplemented(self):
        c = gvMultiprocessing.Workflow()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName', '-n', '']
    print(os.getenv('PYTHONPATH'))
    unittest.main()
