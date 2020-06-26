"""
Created on May 27, 2020

@author: Jonathan Gossage

This module contains definitions that allow modules that run in a Global
Village test environment to find the information that they need to function
without having to examine low-level system idiosyncratic data.
"""

class gvEnvironmentError(Exception):
    """
    Generic exception to raise and log fatal errors building a Global Village
    environment.
    """
    def __init__(self, msg : str) -> None:
        super().__init__()
        self.msg = f"E: {msg}"
    def __str__(self) -> str:
        return self.msg


# Define names of environment variables used in a GlobalVillage test
# environment

"""Major system type such as Linux or Windows"""  #pylint: disable=pointless-string-statement
GVSYSTEM          = 'GVSYSTEM'
"""
Name of the computer node this environment is run on. Note that the environment
may have been created on a different machine than the one that it is running
on.
"""
GVNODE            = 'GVNODE'
"""Name of the distributor of the Linux distribution being used"""
gvDistributorName = 'gvDistributorName'
"""Description of this Linux release"""
gvDistroDesc      = 'gvDistroDesc'
"""Distribution release number of this Linux distribution"""
GVDISTRORELEASE   = 'GVDISTRORELEASE'
"""Distribution codename of this Linux distribution"""
gvDistroCodename  = 'gvDistroCodename'
"""Operating system release number"""
gvOSRelease       = 'gvOSRelease'
"""Operating system release description"""
gvOSReleaseDesc   = 'gvOSReleaseDesc'
"""
Architecture of the machine the environment is running on. This information
relates to the architecture of the main board being used.
"""
gvMachine         = 'gvMachine'
"""
Architecture of the processor the environment is running on. This information
is frequently the same as for the machine since, as far as I know, no main
board supports heterogeneous processor types on a single motherboard. It is
often not supplied, depending on the nature of the platform environment so use
the machine architecture instead.
"""
gvProcessor       = 'gvProcessor'
"""The common full name of the operating system in use"""
gvOSName          = 'gvOSName'
"""
Only appears on Linux systems. Indicates whether the Gnu subsystem and related
commands are present. The absence of this specification is not necessarily proof
that GNU is not present, depending on what the Linux distribution decides to
communicate.
"""
gvGnu             = 'gvGnu'
