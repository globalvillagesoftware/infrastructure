"""
Logging Configuration Support

This class will eventually run stand-alone and will provide logging
configuration for an entire physical site, but originally it will simply be
part of the logging system support.

.. only:: development_administrator

    
    Created on Jul. 14, 2020
    
    @author: Jonathan Gossage
"""

from typing import MutableMapping, Any, Callable, Mapping, Optional

import lib.gvLogging
import logging

class gvLoggingConfiguration():
    """
    Manages logging configurations.
    Supports giving names to logging system components such as filters and
    formatters.

    All components, such as `filters`, `formatters` and `handlers`, being
    added to a configuration should be properly customized before being added.
    It is not the job of this software to do the customization. It should be
    done by the user prior to submitting the component to this system.
    
    """
    def __init__(self: 'gvLoggingConfiguration') -> None:
        self._handlers: MutableMapping[str, logging.handler]={}
        self._filters: MutableMapping[str,
                                      Union[logging.Filter,
                                            Callable[logging.LogRecord,
                                                     logging.LogRecord]]]={}
        self._loggers: MutableMapping[str, gvLogging]={}

    def loadConfiguration(self: 'gvLoggingConfiguration',
                          name: str='defaultGVconfig') -> None:
        pass

    def getCfgTree(self: 'gvLoggingConfiguration',
                   loggingName: str) -> MutableMapping[str, Any]:
        pass

    def createFilter(self: 'gvLoggingConfiguration',
                     name: str,  # Name of the filter
                      # The customized class
                     filter_: Optional[logging.Filter]=None,
                     # The environment
                     extra: Optional[Mapping]=None) -> logging.Filter:
        """
        **Python** supports three ways of defining a filter but the |gv| will
        only use one of them. They will use the traditional way by creating
        subclasses  of 'logging.Filter and overriding the 'filter' method in
        the base class without invoking the base class implementation.

        Filters act by examining the 'LogRecord' and the environment and
        determining from this data whether logging of the 'LogRecord' should be
        permitted. 
        
        If your filter needs additional environmental information, you can use
        the optional argument `extra` to supply a dictionary containing this
        information that this method will use to setup the information
        automatically. 

        A given filter may be used with many different logging components such
        as different loggers or handlers.
        """
        if self._filters.get(name,
                             None) is not None:
            raise(ValueError(f'Filter {name} has already'
                             ' been added to the logging configuration'))
        if filter_ is None:
            filter_ = logging.Filter()
        if extra is not None:
            for k, v in extra:
                setattr(filter_, k, v)
        self.filters[name] = filter_
        return filter_

    def createFormatter(self: 'gvLoggingConfiguration',
                        name: str,  # Name of the formatter
                        style: str='%',
                        validate: bool=True,
                        reset: bool=True,
                        formatter: Optional[logging.Formatter]=None,
                        fmt: Optional[str]=None,
                        datefmt: Optional[str]=None,
                        extra: Optional[Mapping]=None) -> logging.Formatter:
        """
        A given formatter may be used with many different handlers.
        
        Formatters may be customized in number of different ways.
        
        * If all you want to do is to add specific pre-known information to the
          message being logged, then you can simply override the message format
          string for this logger. You pass a custom template to the `fmt`
          argument when you construct a formatter object. This template string
          is used by the standard `formatter` to create the actual message that
          will be logged. See
          https://docs.python.org/3/library/logging.html#formatter-objects for
          details and examples of how this can be done.
        * If you want to do custom formating of date/time information, you can
          do this by passing a custom template to the `datefmt` argument when
          you construct a `formatter` object. The default is to display
          date/time information time based on the local time zone where the
          logging message was generated. If your organization or the software
          that you are monitoring is used in many time zones, you may prefer to
          see date/time information in UCT rather than in local time. The
          **Python** document referred to above covers the details of this
          topic.
        * The **Python** formatter understands a variety of contextual
          information that you may want to include in your logged messages and
          it stores such information internally as formatting attributes that
          can be referred to from templates. See the above **Python**
          documentation for details. you can supplement this information in a
          `formatter` in two ways:

          * You can add this information manually when creating a `formatter`
            object. Thus `setattr(formatter, info-name, info-value)` would
            create an attribute called `info-name` with a value of
            `info-value`.
          * You can add this information while using this method. This method
            has an additional optional argument called `extra` that accepts a
            dictionary that defines the additional attributes to be held in a
            `formatter` and will place them in the `formatter` for you.
          * You may need more radical customization. In this case you can
            create a custom `formatter`, derived from the standard `formatter`
            and you can override the following methods:
        
            * format |br| 
              Handles the basic formatting of a message.
            * formatTime |br| 
              Handles the formatting of date and time information.
            * formatException |br| 
              Formats the exception information that may be added to a logging
              message.
            * formatStack |br| 
              Formats the stack information that may be added to a logging
              message.

            See the **Python** documentation above for more details.
        """
        if self._formatters.get(name,
                                None) is not None:
            raise(ValueError(f'Formatter {name} has already'
                             ' been added to the logging configuration'))
        if formatter is None:
            formatter = logging.Formatter(fmt,
                                          datefmt,
                                          style=style,
                                          validate=validate)
        if extra is not None:
            for k, v in extra:
                setattr(formatter, k, v)
        self.formatters[name] = formatter
        if reset:
            """
            * Should use the base **Python** implementation
            * Should use the **Python** default formatting strings.
            * Should use the default **Python** formatting insertion style.
            
            It seems the best way to do this is to get rid of the old formatter
            and substitute a new one. This means that all references to the old
            formatter should be changed to the new formatter. We can determine
            what references exist from the configuration.
            
            This should be done in the following order:
            
            * Allocate a new formatter based on what is requested of the method.
            * Walk the configuration tree creating references to the new
              formatter.
            """
            pass
        return formatter

    def createHandler(self: 'gvLoggingConfiguration',
                      name: str):  # Name of the handler
        """
        A given handler type may be used with many different loggers. Thus a
        `StreamHandler` could be used in many different places. It would be a
        mistake to assume that the handler associated with one logger is the
        same as a handler associated with some other logger. This is so because
        the handlers are amenable to different customizations such as logging
        level sensitivity or filtering that ensure that the handler works
        properly in a given environment. Also, handlers are subject to runtime
        configuration changes and the nature of these changes may be sensitive
        to the location of the handler in the logging hierarchy. All this means
        that it is difficult to share handlers of similar types in different
        parts of the logging hierarchy and thus that most, if not all, handlers
        should be unique. 

         If a handler is not given a filter, a default filter that allows
          everything is supplied.
        """
        pass

    def createLogger(self: 'gvLoggingConfiguration',
                     name: str):  # Name of the logger
        """
        The |gv| logging class was established early during initialization and
        all loggers created by 'logging.Logger' will be of the correct type.

        Loggers are unique and should only appear once in a logging hierarchy.
        There is no logger object sharing as there is with other components of
        he logging system. This is a restriction of the underlying **Python**
        logging system.
        """
        pass


def initializeLogging():
    if not isinstance(logging.getLoggerClass(),
                      lib.gvLogging.gvLogging):
        logging.setLoggerClass(lib.gvLogging.gvLogging)

initializeLogging()

