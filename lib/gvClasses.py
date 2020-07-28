"""
Miscellaneous classes used throughout the |gv| codebase.

.. only:: development_administrator

    Created on Jul. 24, 2020
    
    @author: Jonathan Gossage
"""

class Counter(int):
    """
    Implements an integer that is used as a counter. A counter counts
    the number of occurrences of an object or an event in a particular
    context. Counters usually increment the count by 1. It is the high-runner
    case that objects are added to or removed from a context, one-by-one. But
    it is not uncommon to add or remove groups of objects at the same time.
    This is why the Counter class is sub-classed from integers, since the
    generalized operations of addition and subtraction work very well as the
    means of recording the addition or removal of items in a context.
    """
    def __init__(self: 'Counter',
                 item: int = 0):
        self._item = item

    def Count(self: 'Counter',
              increment: int = 1):
        """If you want to count down, make the increment negative"""
        self._item += increment
        return self._item
