"""
The **Global Village** interface to **Python** logging.

See :ref:`logging-section` for a survey of the principles that underly
logging and their use in a **Python** environment. See also
https://docs.python.org/3/library/logging.html for the **Python** documentation
on their logging module.

.. only:: development_administrator

    Module management
    
    Created on Apr. 30, 2020
    
    @author: Jonathan Gossage
"""

from typing import (Optional, Dict, Tuple, Union,
                    MutableMapping, Sequence, Any)
import logging

__ALL__ = ['getLogger']

class gvLogging(logging.Logger):
    """
    This class is only used to verify that loggers have been initialized to
    |gv| standards. The existence of the `initialized` instance attribute is
    used to verify that the class has been properly initialized.
      
    """
    def __init__(self: 'gvLogging',
                 name: str) -> None:
        super().__init__(name)
        self._handlers: MutableMapping[str,  # Handler Name
                                       Tuple[logging.Handler,
                                        Optional[logging.Filter],
                                        Optional[logging.Formatter]]] = {}

    def addHandler(self: 'gvLogging',
                   handler: logging.Handler,
                   name:str) -> None:
        super().addHandler(handler)
        self._handlers[name] = handler

    def modifyHandler(self: 'gvLogging',
                      name: str,
                      filter_: Optional[Union[logging.Filter,
                                              Sequence[logging.Filter]]]=None,
                      formatter: Optional[logging.Formatter]=None,
                      level: Optional[int]=None) -> None:
        if filter_ is not None:
            if isinstance(filter_, Sequence):
                for f in filter_:
                    self._handler[name].addFilter(f)
            else:
                self._handlers[name].addFilter(filter_)

        if formatter is not None:
            self._handlers[name].setFormatter(formatter)

        if level is not None:
            self._handlers[name].setLevel(level)

        if filter_ is None and formatter is None and level is None:
            super().warning('No attributes of handler'
                            f' {name} requested to be modified')

    def addFilter(self: 'gvLogging',
                  filter_: logging.Filter,
                  name: str,
                  toLogger: Optional[Sequence[str]]=None,
                  toHandler: Optional[Sequence[str]]=None) -> None:
        if toLogger is None:
            self._filters[name] = filter_
            super().addFilter(filter_)
        if toHandler is not None:
            for h in toHandler:
                h.addFilter(filter_)
                self._filters[name] = filter_

    def __del__(self):
        """
        Do cleanup before exiting
        """
        if getattr(self,
                   self._handlers,
                   None) is not None:
            for h in self._handlers:
                self.removeHandler(h)
                del h
            delattr(self, self._handlers)
        super().__del__()


def initializeLogger(name: Optional[str],
                     cfg=MutableMapping[str, Any]) -> gvLogging:
    """
    Initializes a logger in the logging hierarchy for this logger.
    Uses a dictionary as a source for a description of the desired
    configuration. This dictionary is structured identically to that used by
    **Python** logging to determine the configuration of a logging tree. The
    difference is that interpretation of this dictionary is completely provided
    by the |gv|. This change supports the elimination of anonymous components
    and is preparation for the full support of incremental logging
    configuration for long running applications that may run for weeks or
    months without application termination.
    """
    pass


def prepareLogging(name: str) -> None:
    """
    This is a recursive function that ensures that all ancestor loggers to this
    logger have been properly initialized. The recognition of initialization is
    done in the following way.
    
    A subclass of `logging>logger` is implemented for all loggers supported by
    the |gv|. The only purpose of this class is to be able to check that an
    instance of a logger is an instance of this class. If, instead, it is an
    instance of `logging.Logger` it can be assumed that the named class has not
    been initialized.
    
    During the descent of the tree represented by the logger name, nothing
    happens. All the work is done on the way out. It is here that each logger
    is initialized, based on the configuration data that has been supplied in
    the site environment. This recursion continues until:
    
    * The root organization logger is reached.
    * An initialized logger is found.

    On the way out, a logger is initialized by creating a new logger based on
    the class defined by the |gv|. 
    """
    # Get the name of the parent logger.
    parent: str = name.rpartition('.')[0]
    if parent != '':
        prepareLogging(parent)  # Handle parent logger by recursing
        # We can now initialize this logger because we are on the way out
        initializeLogger(parent)
    else:  # We have reached the root of the logging hierarchy and need to
        # check the root logger
        initializeLogger(None)


    def getLogger(name: str,
                  level=logging.INFO,
                  propagate=False,  # Propagation from logger to logger stops
                                    # here. This ensures that our messages do
                                    # not get handled by loggers that we do not
                                    # control.
               # The default handler will log to stderr
               handler: Optional[Union[Tuple[logging.StreamHandler, str],
                        Sequence[logging.StreamHandler]]]=None,
               # The filter that will be used by this logger
               filter_: Optional[Union[Tuple[logging.Filter, str],
                                       Sequence[Tuple[logging.Filter,
                                                      str]]]]=None,
               # The formatter that will be used by this logger
               formatter: Optional[Tuple[logging.Formatter, str]]=None) ->\
                    logging.Logger:
        """
        This function always creates a user logging environment when invoked.
        It always assumes that the root logger is owned by **Python** and that
        the |gv| will never disturb it. A root for the user's environment will
        be established if it is needed. Many different organizations that have
        supplied software to this environment can live together, each with
        their own logging environment. The optional `handlers`, `fIlters` and
        `formatters` only apply to the leaf logger, not to any of it's parents.
    
        This function can establish the configuration for organization root
        loggers automatically. A check is made to see if if the organization
        root logger exists. If the `logger` returned by the
        `gvLogging.get Logger()` call does not have an associated handler, it
        will be assumed that the root logger has not been initialized and that
        initialization of this logger is needed.
        
        The logging configuration process uses the following sources of
        information:
    
        * Site configuration Files
        * Application specific site configuration files
        * User configuration files that can override the settings in the site
          configuration files.
        * Optional arguments provided to this function.
    
        The various configuration file are merged together in the order
        described above, thus establishing the priority of each configuration
        file. It is important for logging to become available very early in the
        application initialization process so that any initialization errors
        can be handled in a useful way. The **Python** logging environment
        provides a logger of last resort that logs to stderr, but this may not
        be a suitable escape hatch for many applications or organizations and
        also has the limitation that the Python logging module must be imported
        before this facility can happen. This will normally be the case if the
        application uses **Python** logging.
        
        It is planned that this configuration should be overridable by site and
        application configuration items obtained from the application
        configuration process and the command line. but this capability will
        not be available in the initial release.
        """
        # Makes sure that all loggers in the tree are properly initialized.
        prepareLogging()
        _gl = logging.getLogger(name)  # Get our handler
        if _gl.getEffectiveLevel() < level:
            _gl.setLevel(level)
        if not _gl.hasHandlers():  # Add a handler 
            _gl.addHandler(handler)
        if filter_:
            _gl.addFilter(filter_)  # Add a filter
        if formatter:
            if handler:
                handler.addFormatter(formatter)  # Add a formatter
        _gl.propagate = propagate
        return _gl
