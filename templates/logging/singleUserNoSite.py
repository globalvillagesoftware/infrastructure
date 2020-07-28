"""
*jinja2* template for single user logging with no site or organization.

Generates a logging configuration.

.. only:: development_administrator

   Created on Jul. 16, 2020
   
   @author: Jonathan Gossage
"""

from typing import Dict, Any

from lib.configuration import nologging

# Logging configuration keywords
configuration = 'configuration'

template: Dict[str, Any] = { configuration : {nologging : False},
                           }