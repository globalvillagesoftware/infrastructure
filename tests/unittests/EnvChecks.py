"""
Created on Jun. 26, 2020

@author: Jonathan Gossage
"""

import sys

import unittest


class Test(unittest.TestCase):

    def testSuccess1(self):
        self.assertTrue(True)

    def testSuccess2(self):
        self.assertTrue(True)

    def testSuccess3(self):
        self.assertTrue(True)


ret = 0
if __name__ == '__main__':
    import lib.gvTest
    ret = lib.gvTest.gvTestController(caller='tests.unittests.EnvChecks')
    sys.exit(0 if ret.wasSuccessful() else 1)
