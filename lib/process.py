"""
A process is a piece of work written in some other language than *Python*.

An example is running a *Unix* command such as `ls -al` from within a
**Python** application. Another example might be running a graphical
application such as *Gimp* as part of a *Python* based workflow where the
output from the graphical application is used in the rest of the workflow that
is being controlled by *Python*. Processes are actually started and controlled
by the operating system that is providing the environment for the workflow.



Created on Jun. 20, 2020

@author: jgossage
"""


class command():
    """
    """
    pass


class pipeline():
    """
    """
    def __init__(self,
                 *proccess):
        """
        :param command *process: A list of commands that make up the pipeline
        """
        pass

    def connect(self,
                method,
                source,
                target):
        """
        :param method: The method of connecting the commands
        :param source: The source of the connection
        :param target: The target of the connection
        """
        pass


class network():
    """
    """
