"""
Interface to Python logging.

The standard logging system, supplied by Python is very flexible but does not
handle certain cases well. To understand why this is so, lets review the
functionality that needs to be supplied by a logging system.

Logging system needs
====================

Logging system principles
=========================

There are three basic matters to be considered when logging:

* Why should a message be logged?
* What does the message look like?
* Where should the message go?

Logging message applicability
-----------------------------


Logging message appearance
--------------------------

Lets look at the implications within the question, `What should logging
messages look like?`

There are two parts to a logging message:

* Application system specific information
* Logging system specific information

Application specific information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Logging system specific information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Logging message destination
---------------------------
The logging system can be configured to write all logging messages to stderr
and this will be the default configuration if nothing more complex is
supplied.
The configuration of the logging system will be read from the configuration
data and setup in the Logging initializer. We make use of the Python logging
system by default but this can be overridden by the user if a different logging
system is desired.

Python logging system design
============================

Application logging system design
=================================

Wrapup
======

Design principles
-----------------

.. only:: development_administrator

    Module management
    
    Created on Apr. 30, 2020
    
    @author: Jonathan Gossage
"""

import logging
from typing import Optional, Dict, Union

import lib.configuration as _c

gvLogName = 'Global Village'
gvHandler = 'gvHandler'
gvLogger: Optional[Union[logging.Logger, 'Logging']] = None

__ALL__ = ['set_logging', 'Logging', 'getLogging']

#NOTE: Remove the dependence on the configuration


def setLogging(name: Optional[str]=gvLogName,
               level=logging.INFO,
               propogate=False,     # Propagation from logger to logger stops
                                    # here. This ensures that our messages do
                                    # not get handled by loggers that we do not
                                    # control.
               # The default handler will log to stderr
               handler: logging.Handler=logging.StreamHandler(),
               # The filter that will be used by this logger
               filter_: Optional[logging.Filter]=None,
               # The formatter that will be used by this logger
               formatter: Optional[logging.Formatter]=None) -> logging.Logger:
    """
    This function always creates the Global Village logger when none is
    requested. This ensures that the Global Village environment will never
    intrude on other users of the logging system by setting up the root *Global
    Village* logger with `no-propagate`, to ensure that all *Global Village*
    messages will be logged within the *Global Village* logging environment and
    will not escape to the root logger that might have been modified by some
    other user. Any request to create a child of the root logger will be forced
    to to have `propagate` set, permitting delegation to the root logger. This
    function can be used before the standard *Global Village* logging
    environment has been created since there is a dependency between the
    standard *Global Village* logging environment and the the *Global Village*
    configuration which contains a variable that can suppress logging.

    :param str name: The name of the logger requested. It should have the
                     format of a logger e.g. rootLogger.myLogger. If the name
                     does not contain the name of the Global Village root
                     logger that name will be appended. If it is `None`, the
                     root logger for the Global Village environment will be
                     assumed.
    """
    _gl = logging.getLogger(name)  # Get our handler
    if _gl.getEffectiveLevel() < level:
        _gl.setLevel(level)
    if not _gl.hasHandlers():  # Add a handler if none configured
        _gl.addHandler(handler)
    if filter_:
        _gl.addFilter(filter_)
    if formatter:
        _gl.addFormatter(formatter)
    _gl.propogate = propogate
    return _gl


class Logging(object):
    """
This class is only minimally implemented at this stage.

It simply provides the  writing of text to stderr.
It establishes logging on stderr very early so all code in the application,
including early startup code can use logging, thus giving a single interface
to the logging facilities for the application. This class always creates the
root logger for the Global Village environment and may initialize the rest of
the logging environment from the configuration file.
    """

    def __init__(self,
                 propogate=False,
                 verbose=0) -> None:
        self._cfg: Dict[str, CfgEntry] = {}
        self._level: int = self.effectiveLevel(verbose)
        self._logger: logging.Logger = logging.getLogger(gvLogName)
        self._handlers: Dict[str, logging.Handler] = {}
        if self.logger.handlers:
            self._handlers: Dict[str, logging.Handler].update(
                {gvHandler: self._logger.handler})
        else:
            self.addHandler(gvHandler,
                            logging.StreamHandler())
        self._logger.propogate = propogate

        #TODO: Provide the rest of the logging system initialization
        # The rest of the logging initialization. The big item is
        # the definition of the loggers used by a specific
        # application. This setup cannot be performed until
        # configuration data defining the logging configuration becomes
        # available.
        pass

    def effectiveLevel(self,
                       verbose: int=0) -> int:
        _level = logging.WARNING
        if self._cfg and not self._cfg.get(_c.debug):
            if verbose == 0:
                _level = logging.WARNING
            elif verbose >= 1 and verbose <= 2:
                _level = logging.INFO
            else:
                _level = logging.DEBUG
        else:
            _level = logging.DEBUG
        return _level

    def defaultLoggingLevel(self,
                            verbose: int=0) -> int:
        """
        Sets the default logging level based on the verbosity and the
        application execution status such as debugging. This affects both the
        logger and its associated handler.
        :param int verbose: The verbosity level desired
        :returns: Nothing
        """

        _level = self.effectiveLevel(verbose)

        self.logger.setLevel(_level)
        self.handler.setLevel(_level)

    @property
    def logger(self) -> Optional[logging.Logger]:
        """
        :returns: The actual logging system being used
        """
        return self._logger

    @property
    def handler(self) -> Optional[logging.Handler]:
        """
        :returns: The primary handler associated with the underlying logger
                  If the underlying logging system has no concept of handlers
                  None will be returned.
        """
        return self._handler

    def debug(self,
              msg: str,
              *args,
              **kwargs) -> None:
        """
        Consult the Python documentation for logging.debug for details
        """
        self._logger.debug(msg,
                           *args,
                           **kwargs)

    def info(self,
             msg: str,
             *args,
             **kwargs):
        """
        Consult the Python documentation for logging.info for details
        """
        self._logger.info(msg,
                          *args,
                          **kwargs)

    def warning(self,
                msg: str,
                *args,
                **kwargs) -> None:
        """
        Consult the Python documentation for logging.warning for details
        """
        self._logger.warning(msg,
                             *args,
                             **kwargs)

    def error(self,
              msg: str,
              *args,
              **kwargs) -> None:
        """
        Consult the Python documentation for logging.error for details
        """
        self._logger.error(msg,
                           *args,
                           **kwargs)

    def critical(self,
                 msg: str,
                 *args,
                 **kwargs) -> None:
        """
        Consult the Python documentation for logging.critical for details
        """
        self._logger.critical(msg,
                              *args,
                              **kwargs)

    def exception(self,
                  msg: str,
                  *args,
                  **kwargs) -> None:
        """
        Consult the Python documentation for logging.exception for details
        """
        self._logger.exception(msg,
                               *args,
                               **kwargs)

    def log(self,
            level: int,
            msg: str,
            *args,
            **kwargs):
        """
        Consult the Python documentation for logging.log for details
        """
        self._logger.log(level,
                         msg,
                         *args,
                         **kwargs)

    def addHandler(self,
                   name: str,
                   hdlr: logging.Handler) -> None:
        """
        Adds a handler to the list of handlers for this Logging module.
        """
        self._handlers.update({name : hdlr})
        self._logger.addHandler(hdlr)

    @property
    def handlers(self) -> Dict[str, logging.Handler]:
        return self._handlers

    def setEffectiveLevel(self,
                          verbose=-1):
        _level = self.effectiveLevel(verbose if verbose >= 0 else 0)
        self._level = _level
        if self._logger:
            self._logger.setLevel(_level)
        if self._handler:
            self._handler.setLevel(_level)


def initializeLogging() -> Logging:
    logger = Logging()
    global gvLogger
    gvLogger = logger
    return logger


def getLogging() -> Union[logging.Logger, Logging]:
    """
    This is the normal way for a class or module to discover the logging
    environment. Using this function ensures that the user need not be
    concerned about the state of the logging environment
    """
    if not gvLogger:
        setLogging(gvLogName)
    return gvLogger

