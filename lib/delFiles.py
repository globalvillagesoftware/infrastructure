"""
Created on Jun. 17, 2020

@author: jgossage
"""

from pathlib import Path
import sys

class delFiles():

    def __init__(self, files=[], prefix=Path('need_a_valid_directory'),
                 sudo=False, recursion=False, verbosity=0):
        self._valid = True
        p = Path(prefix)
        p.expanduser()
        if not p.is_dir():
            print(f'delFiles - The prefix {str(prefix)} is'
                  ' not an existing directory',
                  file=sys.stderr)
            valid = False
        self._prefix = prefix
        self._sudo = sudo
        self._recursion=recursion
        self._options=''

    def __call__(self, files=[]):
        ret = 0
        if not self._valid:
            print('delFiles - Not able to process'
                  ' commands. error occurred previously')
            return 1
        for f in files:
            if not f.exists():
                print(f'')
        return ret
