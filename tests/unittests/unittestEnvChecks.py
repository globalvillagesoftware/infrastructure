"""
Created on Jun. 26, 2020

@author: Jonathan Gossage
"""

import sys

import unittest


class Test(unittest.TestCase):

    def testSuccess(self):
        self.assertTrue(True)

    def testFailure(self):
        self.assertTrue(False)

    def testError(self):
        raise ValueError('Shows an error in unit tests')


ret = 0
if __name__ == "__main__" or __name__ == 'unittests.unittestEnvChecks':
    import lib.gvTest
    print(f'About to do testing - in {__name__}')
    ret = lib.gvTest.gvTestController(caller=f'{__name__}')
    sys.exit(ret)
