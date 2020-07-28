"""
Test driver for gvLogging

This test should be run in a virtual machine since it sets up dummy loggers in
the standard **Python** logging environment. If the tests are run in a virtual
machine, the various test loggers will disappear when the virtual machine is
shutdown. If it is run on a standard development machine, the machine should be
rebooted after the tests to get rid of the test loggers. This ensures that
testing always takes place in a clean, reproducible environment.

.. only:: development_administrator
    
    Created on Jul. 11, 2020
    
    @author: Jonathan Gossage
"""

import unittest

import lib.gvLogging as _l


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSetupLogging(self):
        pass

    def testInitializeLogging(self):
        pass


if __name__ == '__main__':
    unittest.main()