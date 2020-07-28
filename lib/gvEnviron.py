"""
Miscellaneous environment definitions

These definitions have proven helpful to |gv| programming. They are constructs
that could have been supplied by **Python** but they were deemed not important
enough to do so. Normally, individual definitions will be imported, e.g.
`from lib.gvEnviron import EXC_INFO`. since only a small number of definitions
are likely to be used in any specific instance.

.. only:: development_administrator
    
    Created on Jul. 17, 2020
    
    @author: Jonathan Gossage
"""

from types import TracebackType
from typing import TypeVar, Tuple, Optional

# Typing variables
EXC_INFO = TypeVar(Tuple[Optional[type(BaseException)],
                         Optional[BaseException],
                         Optional[TracebackType]])
"""
The information passed to an exception handler
"""
