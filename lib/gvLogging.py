"""
Interface to Python logging.

The logging system can be configured to write all logging messages to stderr
and this will be the default configuration if nothing more complex is
supplied.
The configuration of the logging system will be read from the configuration
data and setup in the Logging initializer. We make use of the Python logging
system by default but this can be overridden by the user if a different logging
system is desired.

Created on Apr. 30, 2020

@author: Jonathan Gossage
"""

import logging
from typing import Optional, Dict

import lib.configuration as _c

gvLogName = 'Global Village'
gvHandler = 'gvHandler'

#NOTE: Remove the dependence on the configuration


def setLogging(name: Optional[str]=None,
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
    This function is platform and software vendor neutral.
    If the user does not supply the name of a logger to be created, it will
    create the Global Village logger.
    """
    _gl = logging.getLogger(gvLogName)  # Get our handler
    if _gl.getEffectiveLevel() < level:
        _gl.setLevel(level)
    if not _gl.hasHandlers():  # Add a handler if none configured
        _gl.addHandler(logging.StreamHandler())
    if filter:
        _gl.addFilter(filter_)
    if formatter:
        _gl.addFormatter(formatter)
    _gl.propogate = propogate
    return _gl


class Logging(object):
    """
This class is only minimally implemented at this stage. It simply
provides the  writing of text to stderr.
It establishes logging on stderr very early so all code in the application,
including early startup code can use logging, thus giving a single interface
to the logging facilities for the application. This class always creates the
root logger for the Global Village environment and may initialize the rest of
the logging environment from the configuration file.
    """

    def __init__(self,
                 cfg: _c.Configuration,
                 propogate=False,
                 verbose=0) -> None:
        self._cfg = cfg
        self._level: int = self.effectiveLevel(verbose)
        self._logger: logging.Logger = logging.getLogger(gvLogName)
        if self.logger.handler:
            self._handlers: Dict[str, logging.Handler] = {gvHandler:
                                                          self._logger.handler}
        else:
            self.addHandler(logging.StreamHandler)
        self._logger.propogate = propogate

        # Get access to configuration variables stored in the configuration
        # module,
        if cfg is None or not _c or _c.nologging not in cfg or\
                not self._cfg.get(_c.nologging):
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
                           args,
                           kwargs)

    def info(self,
             msg: str,
             *args,
             **kwargs):
        """
        Consult the Python documentation for logging.info for details
        """
        self._logger.info(msg,
                          args,
                          kwargs)

    def warning(self,
                msg: str,
                *args,
                **kwargs) -> None:
        """
        Consult the Python documentation for logging.warning for details
        """
        self._logger.warning(msg,
                             args,
                             kwargs)

    def error(self,
              msg: str,
              *args,
              **kwargs) -> None:
        """
        Consult the Python documentation for logging.error for details
        """
        self._logger.error(msg,
                           args,
                           kwargs)

    def critical(self,
                 msg: str,
                 *args,
                 **kwargs) -> None:
        """
        Consult the Python documentation for logging.critical for details
        """
        self._logger.critical(msg,
                              args,
                              kwargs)

    def exception(self,
                  msg: str,
                  *args,
                  **kwargs) -> None:
        """
        Consult the Python documentation for logging.exception for details
        """
        self._logger.exception(msg,
                               args,
                               kwargs)

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
                         args,
                         kwargs)

    def addHandler(self,
                   name: str,
                   hdlr: logging.Handler) -> None:
        self._handlers.update(name, hdlr)
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
