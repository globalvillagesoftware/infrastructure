# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configurationx.html
from docutils.parsers import rst

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('../../../src'))


# -- Project information -----------------------------------------------------

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# This is the only manual change that is needed. Change the name of the project
# appropriately. Possibly, the name of the author.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
project = 'Global Village'
author = 'Jonathan Gossage'
copyright = f'2020, {author}'

# The full version, including alpha/beta/rc tags
release = '0.1.0'


# -- General configurationx ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_rtd_theme',
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# These are RST substitutions that are used throughout the Global Village
# documentation.
rst_prolog = """
.. |br| raw:: html

   <br />
   
"""

# These are links to external documents and services that can be accessed from
# any document in the Global Village document system.
rst_epilog =  """
.. _Python:  https://www.python.org/
.. _Python Package Index: https://pypi.org
.. _JSON: https://www.json.org/json-en.html
.. _Eclipse Marketplace: https://marketplace.eclipse.org/
.. _Eclipse Download: https://www.eclipse.org/downloads/
"""


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The location of CSS Global Village Overrides to the Read The Docs theme for
# Sphinx
html_css_files = ['css/custom.css']

# Options that control hw the sphinx_rtd_theme displays.
html_theme_options = {
    'prev_next_buttons_location': 'both',
    'collapse_navigation': False,
    'navigation_depth': 4,
    'display_version': True,
    'logo_only': False,
    'titles_only': False,
    'style_nav_header_background': 'moccasin',
    'sticky_navigation': True,
    'includehidden': False  
}

# -- Extension configurationx -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configurationx for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/3/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True