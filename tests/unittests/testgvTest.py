"""
Exhaustive test of gvTest

.. only:: development_administrator

    Module management
    
    Created on Jun. 27, 2020
    
    @author: Jonathan Gossage
"""

import sys
import unittest


class Test(unittest.TestCase):

    def testName(self):
        pass


if __name__ == "__main__":
    import lib.gvTest
    ret: unittest.TestResult =\
        lib.gvTest.gvTestController(caller='tests.unittests.testgvTest')
    sys.exit(0 if ret.wasSuccessful() else 1)
