"""
Created on May 27, 2020

@author: Jonathan Gossage
"""
import os
import unittest

# This import actually runs the code inside the module determineEnvironment
# since it is all module level code and thus gets executed at import time.
# However it is never referenced since we have other methods of checking that
# the unit test worked.
import determineEnvironment as de
import environmentAccess as ea


class Test(unittest.TestCase):


    def testDetermineEnvironment(self):
        ux = 'Unexpected platform data format'
        self.assertEqual(os.environ[ea.gvSystem].lower(), 'linux',
                         msg=f'{ux} - system name')
        self.assertEqual(os.environ[ea.gvNode].lower(), 'jfgper', msg=)
        self.assertRegex(os.environ[ea.gvRelease].lower(), r'', msg)
        self.assertEqual(os.environ[ea.gvRelease].lower(), '')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDetermineEnvironmentName']
    unittest.main()