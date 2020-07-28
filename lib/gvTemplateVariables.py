"""
*Jinja2* template variables

These variables will normally be accessed from **Python** scripts that turn
templates into modules. They are defined here so that they may also be accessed
directly from **Python** code.

.. only:: development_administrator

    Created on Jul. 17, 2020
    
    @author: Jonathan Gossage
"""

from sys import version_info as vi

# Template variables
python-39 = '3.9'
python_38 = '3.8'
python_37 = '3.7'
python_36 = '3.6'
python_35 = '3.5'
python_34 = '3.4'
python_33 = '3.3'
python_32 = '3.2'
python_31 = '3.1'
python_30 = '3.0'
python_version = lambda: f'{vi.major}.{vi.minor}.{vi.micro}'