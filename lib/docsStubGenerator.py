"""
Module documentation stub generator

Has the following characteristics and provides the following capabilities:

1. Generate stub files for each package/module encountered.
   If we have a package, the docstring from the `__init__` module will be used.
   we loop through the package generating stub files for each module or package
   found in the source.
   Individual packages will be treated like modules.
   Stub files will be generated using *Jinja2* templating.
   Stub files must be compiled with *Sphinx* before being used. Compilation can
   be an automatic step handled by this program.
   Each stub file will be a `.rst` file.
   For each stub file generate things using the following structure:
   
   1. The title line should be constructed from the first line of the
      docstring.
   2. A automodule directive is inserted.
   3. For each module level function a autofunc directive is included.
   4. Only functions, classes and module attributes specified in the `__ALL__`
      variable will be included.
   5. For each class an autoclass directive is included. For each class method
      and class attributes will be displayed.
   6. For each method in a class, the method docstring along with the method
      signature and method attributes will be displayed.
   7. The final result will be a stub file giving access to the documentation
      for all items contained in the module.

2. An index file will be generated that will give access to all the modules in
   the package, including nested packages and modules. This will be a standard
   `.rst` file. It can be used to control access to the package/module
   documentation and can be included in the root table of contents for a
   document.
3. This module is a library module and has no input/output capability.
   The caller should provide those. In addition, the caller is responsible for
   making the correct contents from SCM repositories made available in source
   file format.

Object structure
================

Namespace packages
------------------

Namespace packages may have several parts that reside at different parts of the
file system. Each part can be treated in the same way as ordinary *Python*
packages. They have the following attributes:

* Namespace package parts have no `__init__.py` file in their home directory.
  This is an essential feature for recognizing namespace package parts.
* Namespace packages may nest. In other words they may be included in a parent
  namespace, either in an ordinary package or in a namespace package.
* The path to a namespace part must be unique except that it can pass through
  one or more namespace packages.
* Module names are insensitive to the fact that namespaces potentially have
  many parts.
* Namespace packages must include one or more *Python* modules or package
  directly or indirectly. Directories that do not meet these criteria are
  ordinary directories
* All namespace packages share the same prefixes to their name differing only
  in their source folder root.
* Duplicate modules are not supported, otherwise the qualified name of a module
  could not be unique.
* Namespace packages are important to this program because their recognition
  makes it possible for us to verify module and package names
* In all other respects, namespace packages are identical to normal packages.

Ordinary packages
-----------------

These packages always have a `__init__.py` file in their root directory. They
are self contained. Package contents must reside in or below the package
directory.

Modules
-------

Modules are essentially *Python* source files. Modules contain the actual
documentation we need in their `docstrings`.

Finding Packages
================

Packages must be found on the file system or in SCM repositories. It is
legitimate to find some or all of the packages in particular parts of an SCM
repository. This can help to ensure that the documentation and the source code
for a release are in sync.

`SCMs` are handled by cloning the required branch of the repository and
creating a local workspace. Thus the contents from repositories can be treated
in exactly the same way as other document sources. Acquiring and cloning
repositories is essentially a pre-processing step. All temporary repository
clones are automatically deleted when the application terminates, normally or
abnormally. `SCMs` are not actually handled in this module which expects all
its input to be standard *Python* packages and modules.

.. only:: development_administrator

    Module management
    
    Created on Jun. 28, 2020
    
    @author: jgossage
"""

from pathlib import Path
import re
from typing import Dict, Optional, Sequence, Union

class _PythonPackagingObject():
    """
This is the base class for the objects that are contained in the package tree.
    """

    def __init__(self: '_PythonPackagingObject',
                 path: Path,
                 parent: Optional['_PythonPackagingObject']) -> None:
        self._path = path
        self._parent = parent
        self._name = None

    @property
    def path(self: 'PythonPackagingObject'):
        return self._path

    @path.setter
    def path(self: '_PythonPackagingObject',
             path: Path):
        self._path = path

    @property
    def parent(self: '_PythonPackagingObject') -> '_PythonPackagingObject':
        return self._parent

    @parent.setter
    def parent(self: '_PythonPackagingObject',
               parent: '_PythonPackagingObject'):
        self._parent = parent

    @property
    def moduleName(self: '_PythonPackagingObject') ->str:
        """
        This name cannot be relied on until the entire package tree has been
        constructed as complete information may not be available.
        """
        return self._constuctFullName()



    @property
    def packageName(self: '_PythonPackagingObject') ->str:
        """
        If this object has a parent, return its Python package name,
        otherwise return an empty string.
        """
        if self.parent:
            # Take off the last element of the name to get the parent package
            # name.
            return re.sub(r':+$',
                          self.name,
                          '')
        else:
            return ''  # There is no package name

    def _constructFullName(self: '_PythonPackagingObject',
                           start: Optional[str]=None) -> str:
        """
        Package and module names are always constructed dynamically
        While the package tree is being constructed, we may not have enough
        information to properly construct the name because some directories
        have not been visited yet.
        """
        _name = start if start else self.path.name
        _parent = self.parent
        while _parent:
            _name = _parent.path.name + ':' + _name
            _parent = _parent.parent
        return _name


class _UnknownObject(_PythonPackagingObject):
    """
    We do not have enough information yet to determine what kind of object we
    have. This object will be replaced by the real thing - _NamespacePackage,
    _PythonPackage, or _PythonModule when we figure out what it is. If it is
    none of the above, it will be removed when tree construction is complete.
    """

    def __init__(self: '_UnknownObject',
                 path: Path,
                 parent: Optional[_PythonPackagingObject]):
        super( path,
               parent)

    def remove(self: '_UnknownObject'):
        """
Removes this object from the package Tree. This method is only called for
_UnknownObjects. We now have enough information to set the real type of any of
these objects that are actually Python packages.
        """

        p = self.parent
        if isinstance(p, _UnknownObject):
            pass
        del(self)   # Removes a reference to this object making it more likely
                    # to be a candidate for the garbage collector.


class _NamespacePackage(_PythonPackagingObject):
    """
    """

    def __init__(self: '_NamespacePackage',
                 path: Path,
                 parent: Optional[_PythonPackagingObject]):
        super(path,
              parent)
        # The parts that make up the namespace
        self._parts: Dict[str, _PythonPackagingObject] = {}
        # The packages and directories that are contained directly in this
        # namespace. Includes the contents of all parts.
        self._contents: Dict[str, _PythonPackagingObject] = {}

    @property
    def parts(self: '_NamespacePackage') -> Dict[str, _PythonPackagingObject]:
        return self._parts

    @parts.setter
    def parts(self: '_namespacePackage',
              parts: Dict[str, _PythonPackagingObject]):
        self._parts = parts

    @property
    def contents(self: '_NamespacePackage') -> Dict[str,
                                                    _PythonPackagingObject]:
        return self._contents

    @contents.setter
    def contents(self: '_namespacePackage',
              contents: Dict[str, _PythonPackagingObject]):
        self._contents = contents


class _PythonPackage(_PythonPackagingObject):
    """
    """

    def __init__(self: '_PythonPackage',
                 pkg: Path,
                 parent: Optional[_PythonPackagingObject]):
        super(pkg,
              parent)


class _PythonModule(_PythonPackagingObject):
    """
    """

    def __init__(self: '_PythonModule',
                 mod: Path,
                 parent: Optional[_PythonPackagingObject]):
        super(mod,
              parent)


class StubGenerator:
    """
Generates *Sphinx* compatible documentation and builds the document files
associated with a given set of *Python* source from the docstrings contained in
the source files.
    """

    def __init__(self: 'StubGenerator',
                 output: Optional[Path]=None,
                 docs: Optional[Path]=None,
                 source: Optional[Sequence[Union[Path, str]]]=None,
                 templates: Optional[Sequence[Union[Path, str]]]=None) -> None:
        """
        """
        self._output = output
        self._docs = docs
        self._source = source
        self._templates = templates
        self._packageTree: Sequence[_PythonPackagingObject]=[]

    @property
    def output(self: 'StubGenerator') -> Optional[Path]:
        return self._output

    @output.setter
    def output(self: 'StubGenerator',
               output: Path):
        self._output = output

    @property
    def docs(self: 'StubGenerator') -> Optional[Sequence[Union[Path, str]]]:
        return self._docs

    @docs.setter
    def docs(self: 'StubGenerator',
               docs: Path):
        self._docs = docs

    @property
    def source(self) -> Optional[Sequence[Union[Path, str]]]:
        return self._source

    @source.setter
    def source(self: 'StubGenerator',
               source: Sequence[Union[Path, str]]):
        self._source = source

    @property
    def templates(self: 'StubGenerator') -> Optional[Sequence[Union[Path,
                                                                    str]]]:
        return self._templates

    @templates.setter
    def templates(self: 'StubGenerator',
                  templates: Sequence[Union[Path, str]]):
        self._templates = templates

    @property
    def packageTree(self: 'StubGenerator') -> Sequence[_PythonPackagingObject]:
        return self._packageTree

    @packageTree.setter
    def packageTree(self: 'StubGenerator',
                    tree: Sequence[Union[Path, str]]):
        self._packageTree = tree

    def __call__(self: 'StubGenerator') -> None:
        """
        The main entry point for the application
        """

        # Find out what we have to work with
        self.packageTree = self._ConstructTree()
        # Now build the documentation
        self._generateDocStubs()
        self._generatePackageDocumentation()

    def _SetDirectory(self: 'StubGenerator',
                      parent: _PythonPackagingObject,
                      dir_: Path) -> _UnknownObject:
        """
        Establishes a directory in the package tree before we know all the
        details about it.
        """
        us = _UnknownObject(dir,
                            parent)
        self.packageTree.append(us)
        return us

    def _upgradeUnknownObject(self: 'StubGenerator',
                              parent: _UnknownObject,
                              mod: Path,
                              tree: Sequence[_PythonPackagingObject]):
        """
        Upgrade an _UnknownObject to a package
        """
        pass

    def _getParent(self: 'StubGenerator') -> Optional[_PythonPackagingObject]:
        # The last element in the package tree will be the parent of this
        # module, If the package tree is empty, there will be no parent
        _parent = self.packageTree[-1:-1]
        if len(_parent) == 0:
            _parent = None
        return _parent

    def _HandleModule(self: 'StubGenerator',
                      packageTree: Sequence[Path],
                      mod: Path) -> None:
        """
        Handle a Python Module
        """

        _pythonSuffixes: Sequence[str] = ('py',)

        if mod.suffix not in _pythonSuffixes:
            return  # This is not a module - ignore it

        _parent: Optional[_PythonPackagingObject] = packageTree[-1:-1][0]
        
        # This is a Python module so the parent type can be upgraded to a
        # package.
        if isinstance(_parent, Sequence):
            if len(_parent) == 0:
                _parent = None  # we have no parent
        elif isinstance(_parent, _UnknownObject):
            self.upgradeUnknownObject(_parent,
                                      mod,
                                      self.packageTree)
        elif isinstance(_parent, _PythonPackage):
            pass
        elif isinstance(_parent, _NamespacePackage):
            pass
        
        else:
            raise ValueError(f'Unrecognizable parent {type(_parent)}'
                             f'in package tree for module {str(mod)}')

    def _HandlePackage(self: 'StubGenerator',
                       parent: Optional[_PythonPackagingObject],
                       packageTree: Sequence[Path],
                       pkg: Path) -> None:
        """
        """
        packageTree.append(_UnknownObject(pkg,
                                          parent))

    def _internalConstructStub(self: 'SubbGenerator',
                               source: Path) -> _PythonPackagingObject:
        # Later we will find out if the source directory is really a
        # package. If the source directory is really a file then it will
        # become an entry in the packageTree and will have no parent. Thus
        # it becomes possible to pass in a list of files as sources that
        # are not necessarily in a valid Python package and to handle them.
        # This is probably not a good project structure as other Python
        # processes will not be able to handle such a package structure
        # correctly. It is not a valid Python package. We will report the
        # error but will accept it as the generated documentation may still
        # be useful and needed. The only place where this can happen is at
        # the source level. It is possible that the user made a mistake and
        # that the parent of this module should have been requested as a
        # source. We can actually check this and let the user know what
        # kind of error was made. If we are dealing with a module, the
        # parent must have been a directory and must have been a valid
        # package.
        _packageTree: Sequence[__PythonPackagingObject] = []
        if source.is_dir():
            self._HandlePackage(None,
                                source,
                                _packageTree)
        elif source.is_file():
            # We only get here when the user requested a module directly,
            # rather than starting the request at the package.
            # The parent of this object should have been specified in the
            # sources.
            self._HandleModule(source,
                               _packageTree)
        else:
            return _packageTree  # Skip types we are not interested in

        # Any _UnknownObjects left represent files or directories that have
        # nothing to do with Python so lets get rid of them.
        for p in self._packageTree:
            if isinstance(p, _UnknownObject):
                p.remove()
    
        return _packageTree

    def _ConstructTree(self: 'StubGenerator'):
        """
        Package constructor

        This method walks the source tree provide by the user. It discovers and
        internally records all packages and modules that are present in the
        tree. This tree is constructed initially and provides a fast locator
        for specific packages. Given that the scope of namespace packages
        cannot be established until the entire package tree has been
        constructed, having the tree facilitates testing for the existence of
        modules.
        """
        # Examine the entire source forest, walking it in breadth first mode
        # handling directory contents before handling the directory itself.
        # This loop accepts the possibility that a source object may be a
        # Python package.
        s: Path
        if not isinstance(self.source, Path):
            for s in self.source:
                self.packageTree.extend(self._internalConstructStub(s))
        else:
            self.packageTree.extend(self._internalConstructStub(self.source))

    
    def _generateDocStubs(self: 'StubGenerator') -> None:
        """
        Generate Packaging Document stubs
        """
        pass

    def _generatePackageDocumentation(self: 'StubGenerator') -> None:
        """
        Generate the package documentation
        """
        pass
