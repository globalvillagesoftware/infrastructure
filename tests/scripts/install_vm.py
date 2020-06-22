"""
Created on Apr. 19, 2020

@author: Jonathan Gossage

This module handles the actual creation and configurationx of a virtual machine
for VirtualBox.

@author: jonathan
"""

class Install(object):
    """
    This script automates the process of creating and configuring a new virtual
    machine in VirtualBox.
    """

    def __init__( self, cfg ):
        """
        Constructor
        """
        self._cfg = cfg
        
    @property
    def cfg(self):
        return self._cfg

    def __call__(self):
        return
