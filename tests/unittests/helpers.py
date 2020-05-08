"""
Tests the helper classes in Infrastructure/lib/helpers.py

Created on May 7, 2020

@author: Jonathan Gossage
"""

import os
import unittest
import pathlib as P

from helpers import Helper as hlp
from helpers import GlobalVillageException as gve

class TestHelpers(unittest.TestCase):

    def testUrl(self):
        # Check the creation of the Helper class and the URL property
        h = hlp()
        self.assertEqual(h.url, 'https://github.com/globalvillagesoftware' )

    def testGetRepo(self):

        # Test good invocation of getRepo() with a full path
        p = f'{os.sep}LinuxData{os.sep}EclipseWorkspaces'\
            f'{os.sep}GlobalVillage{os.sep}Infrastructure'
        h = hlp()
        path, name = h.get_repo(p)
        self.assertEqual(path,
                         f'{os.sep}LinuxData{os.sep}EclipseWorkspaces{os.sep}'
                         'GlobalVillage',
                         'get_repo detected an incorrect repository path -'
                         f' {path}')
        self.assertEqual(name, 'Infrastructure',
                         'get_repo detected incorrect repository name -'
                         f' {name}')

        # Test invocation of getRepo with a name only
        path, name = h.get_repo('Infrastructure')
        self.assertEqual(path, '.', 'get_repo Incorrect path - {path} returned')
        self.assertEqual(name, 'Infrastructure',
                         'get_repo detected incorrect repository name -'
                         ' {name}')

        # Test invocation of getRepo with a path only
        path, name = h.get_repo(os.sep)
        self.assertEqual(name, '')
        self.assertEqual(path, os.sep,
                         'get_repo detected incorrect repository path -'
                         f' {path}')


if __name__ == '__main__':
    unittest.main()