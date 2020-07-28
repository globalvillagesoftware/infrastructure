"""
*Jinja2* template to generate custom classes that override `logging.Formatter`.

.. only:: development_administrator

    Created on Jul. 16, 2020
    
    @author: Jonathan Gossage
"""
from types import FunctionType
from typing import Any, MutableMapping

from lib.gvEnviron import EXC_INFO
import lib.gvTemplateVariables

templates:MutableMapping[str: MutableMapping[MutableMapping[str: Any]]] =\
{'FormatterTemplate': {'source':
"""
class {{ FormatterClass }}({{ FormatterBaseClass }}):
    def __init__(self: '{{ FormatterClass }}',
                    fmt: Optional[Union[str, FunctionType[str, str]]]=None,
                    datefmt: Optional[Union[str, Callable[str, str]]]=None,
                    style: str='%',
        {% if python-3.8 >= python-version %}
                    validate:bool=True) -> None
        {% else %}
                ) ->None
        {% endif %}

    def format(self: '{{ FormatterClass }}',
               record: logging.LogRecord)-> logging.LogRecord:
        {% block format %}
        return super.format(record)
        {% endblock %}

    def formatTime(self: '{{ FormatterClass }}',
                   record: logging.LogRecord,
                   datefmt: Optional[[Union[str,
                                            FunctionType[str, str]]=None)\
         -> str:
        {% block formatTime %}
        return super.formatTime(record,
                                datefmt)
        {% endblock %}

    def formatException(self: '{{ FormatterClass }}',
                        exc_info: EXC_INFO) -> str:
        {% block }
        return super.formatException(exc_info)
        {% endblock %}

    def formatStack(self: '{{ FormatterClass }}',
                    stack_info: TraceBackType):
        {% block }
        return super.formatStack(stack_info)
        {% endblock %}
"""
},
'variables': {'FormatterClass' : '',
              'FormatterBaseClass' : 'logging.Formatter',
              'python3.8' : lib.gvTemplateVariables.python_38,
              'python-version' : str(lib.gvTemplateVariables.python_version)}
}
