"""
Functions that interface to a command in a terminal environment

.. only:: development_administrator

    Created on May 27, 2020
    
    @author: jgossage
"""

from lib.gvLogging import Logging as _L


class ShellCommands(object):
    """
    Contains methods that use subprocess to run system commands.
    """

    def __init__(self,
                 params):
        """
        Const
        """
        pass

    def command(self,
                cmd,
                args=[]):
        """Setup the command to be run"""
        _L.critical('command not implemented yet')
        return 1

    def hookupOutputStreams(self,
                            stream):
        """Hookup stdout and stderr"""
        _L.critical('hookupOutputStream not implemented yet')
        return 1

    def hookupInputStream(self,
                          data=None):
        """Supply complete data for stdin"""
        _L.critical('Command not implemented yet')
        return 1

    def run(self):
        """Run the command"""
        _L.critical('run not implemented yet')
        return 1

    def getOutputWhenDone(self,
                          stream,
                          output):
        """Retrieve output when command terminates"""
        _L.critical('GetOutputWhenDone not implemented yet')
        return 1

    def getOutputInProgress(self,
                            stream,
                            block):
        """Retrieves a block of command output while command running"""
        _L.critical('getOutputin Progress not implemented yet')
        return 1

    def supplyInputInProgress(self,
                              block):
        """Supply a block of data to stdin while command is running"""
        _L.critical('SupplyInputIn Progress not implemented yet')
        return 1

    def status(self):
        """Check the status of the command when command completes"""
        _L.critical('status not implemented yet')
        return 1
