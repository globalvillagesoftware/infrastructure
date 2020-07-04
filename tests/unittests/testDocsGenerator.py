"""
Test the docsStubGenerator module

.. only:: development_administrator

    Module management
    
    Created on Jun. 30, 2020
    
    @author: Jonathan Gossage
"""

from pathlib import Path
import unittest

import lib.docsStubGenerator as _sg


class Test(unittest.TestCase):

    def testName(self: 'Test'):
        _sg.StubGenerator(source=Path(\
            "/home/jgossage/EclipseWorkspaces/GlobalVillage/Infrastructure"))()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()