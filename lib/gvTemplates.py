"""
|gv| support for templating, based on *Jinja2*

.. only:: development_administrator

    Created on Jul. 20, 2020
    
    @author: Jonathan Gossage
"""

from importlib import import_module
from types import ModuleType
from typing import Optional, MutableMapping, Any, MutableSequence, Sequence

import jinja2


class Template():
    """
    This represents a template during it's life-cycle.
    A |gv| template is represented externally as a *Python* dictionary with the
    following structure:

    The root of a |gv| template description is a *Python* dictionary that is
    contained in a `TemplateContainer`. This dictionary contains entries where
    the keys are an abbreviated description of the value associated with each
    key. Thus:
    
    * source |br| 
      This is the source code for the template as expected by *Jinja2*. It is a
      multi-line *Python* string. This code contains two components that are
      intermixed.

      * Python source code
      * Jinja2 directives that describe how the *Python* source code is to be
        modified. Actually, *Jinja2* can handle anything that can be
        represented textually, but so far the |gv| is only using it with
        *Python* source code.

    * variables |br| 
      This is a dictionary that contains the definitions of the variables that
      can be used by this *Jinja2* template. The key is the variable name and
      the value is the value of the variable. The value may be a static
      definition such as a number or string, or it can be a *Python* function
      that returns the value. In all cases, the value of the variable must be
      representable as a string since that is what is needed by *Jinja2*.
    """
    def __init__(self: 'Template',
                 name: str):
        self._internalTemplate: Optional[jinja2.Template] = None
        self._renderedSource: Optional[str] = None
        self._content: Optional[ModuleType] = None

        # Import the Python module containing the template
        try:
            self._content: Optional[type.ModuleType] = import_module(name) 
        except ImportError:
            pass

        # Check that the template is usable
        if not self._content or\
           getattr(self._content,
                   'templates') is None or\
           'source' not in self._content.templates:
                raise ValueError(f'The template container {self._name}'
                                 ' does not have any useful content')

        # Do any necessary TemplateContainer level preprocessing
        if 'preprocessing' in self._content:
            self.content['preprocessing']()

        # Compile a Jinja2 template from the source code in this template
        if self._name in self._content.templates:
            self.content.templates[self._name]['internalTemplate'] =\
                TemplateContainer.env.\
                    from_string(self.content.templates['source'])

        # Renders the template into the source code for a Python module. This
        # is what templates are supposed to do.
        self._renderedSource = self._internalTemplate.render()

    def save(self,
             location: str):
        """Save the rendered template output somewhere"""
        pass

class TemplateContainer():
    """
    Contains a related set of templates. A template container is a *Python*
    module with a particular structure. The content of a template container is
    a series of defined Python variables and *Python* functions. The purpose of
    each variable and function is described below:

    * _templates |br| 
      This is a dictionary keyed on template name that contains a complete
      description of a |gv| template.
    * _preprocesing |br| 
      An optional *Python* function that is invoked, if it is present, to
      handle application specific initialization for the entire container. It
      will be invoked before any template initialization is attempted.
    * _postprocessing |br| 
      An optional *Python* function that is invoked, if it is present, to
      handle application specific processing after the templates in a container
      have been written to permanent storage.

    Most containers will simply contain templates.
    """
    env = jinja2.Environment(keep_trailing_newline=True,
                             trim_blocks=False)
    _templates: Sequence[str] = []

    def __init__(self: 'TemplateContainer',
                 name: str,
                 templates: Optional[Sequence[str]]=None):
        self._interestingTemplates: MutableSequence[Template] = []
        self._name = name;
        self._content: MutableMapping[str, ModuleType] = {}
        # Build the template container module if we can
        self._content[self._name] = Template(self._name)
        if self._name in TemplateContainer._templates:
            self._interestingTemplates.append(self._content[self._name])

