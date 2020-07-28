"""
Versioning

Implements `semantic versioning <https://semver.org/>`_.  It implements the
entire specification.  This implementation also implements 'Calendar versioning
<https://calver.org/>`_ and supports hybrid schemes that use elements from both
versioning schemes.

.. only:: development_administrator

    Module management
    
    Created on Apr. 26, 2020
    
    @author: Jonathan Gossage
"""

import re
from typing import Optional, Sequence, MutableSequence, Union, MutableSet, Set

from lib.gvClasses import Counter

class PreRelease(object):
    _choices: MutableSet[str] = ['alpha', 'beta', 'rc']

    @classmethod
    def augmentChoices(cls,
                       choices: set[str]):
        cls._choices.union(choices)

    """
    Implements the pre-release identifier component of a semantic based version
    """
    def __init__(self: 'PreRelease',
                 description: Set[str] = [],
                 counter: Optional[Counter]=None):
        if isinstance(description, str):
            self.validateDescription(description)
            self._descriptionadd(description)
        elif isinstance(description, Set):
            for d in description:
                self.validateDescription(d)
                self._description.add(d)
        else:
            raise ValueError(f'{type(description)} is not a supported type.')
        self._counter = counter

    @property
    def description(self: 'PreRelease')-> MutableSet:
        return self._description

    @property
    def counter(self: 'PreRelease')-> Counter:
        return self._counter

    def __gt__(self: 'PreRelease',
               comparand: 'PreRelease') -> bool:
        for i in range(min(len(self.description),
                           len(comparand.description))):
            if self.description[i] > comparand.description[i]:
                return True
            if self.description[i] < comparand.description[i]:
                return False
            
        if len(self.description) > len(comparand.decription):
            return True
        if self.counter is None and comparand.counter is not None:
            return False
        if self.counter is not None and comparand.counter is None:
            return True
        return False

    def __eq__(self: 'PreRelease',
               comparand: 'PreRelease'):
        for i in range(min(len(self.description),
                           len(comparand.description))):
            if self.description[i] != comparand.description[i]:
                return False
            if len(self.description) ==\
                   len(comparand.description):
                return True
            return True if self.counter == comparand.counter else False
        return False

    def __ne__(self: 'PreRelease',
               comparand: 'PreRelease'):
        return not self. __eq__(comparand)

    def __le__(self: 'PreRelease',
               comparand: 'PreRelease'):
        return not self.__gt__(comparand)

    def __lt__(self: 'PreRelease',
               comparand: 'PreRelease'):
        return not self.__gt__(comparand) and self.__ne__(comparand)

    def __ge__(self: 'PreRelease',
               comparand: 'PreRelease'):
        return self.__gt__(comparand) or self.__eq__(comparand)

    def __hash(self: 'SemanticVersion'):
        calc = (self.description, self.counter)
        return hash(calc)

    def validateDescription(self: 'PreRlease',
                            desc: Union[str, Set[str]]) -> bool:
        """
        This method actually never returns False.  It raises a ValueError
        exception instead that shows an attempt to use a description keyword
        twice in the same pre-release version.  Things like `alpha.alpha` do
        not make a lot of sense. If you really need that form of expression,
        override this method in a derived class and do what you need.
        """
        d = ''
        err = 'Duplicate description terms are not supported. {}'\
            ' is already used.'
        if isinstance(desc, str):
            if self.description in PreRelease.choices:
                return True
            else:
                d = desc
        elif isinstance(desc, Set):
            for d in desc:
                if d not in PreRelease.choices:
                    raise ValueError(err.format(d))
                return True
        raise ValueError(err.format(d))

    def __str__(self: 'PreRelease') -> str:
        string = ''
        for s in self.description:
            string += f'.{s}'
        if self.counter:
            string += f'{self.counter}'
        return string


class Build(object):
    """
    Implements the build identification component of a semantic based version.
    """
    def __init__(self: 'Build',
                 id_: Union[str, Set[str]]) -> None:
        self.id_:Set[str] = {}
        if isinstance(id_, str):
            self._id: Set[str].add(id_)
        elif isinstance(id_, Set[str]):
            for i in id_:
                self._id.add(i)
        else:
            raise ValueError(f'The build id - {id_}'
                             f' has an invalid type - {type(id_)}')

    @property
    def id(self: 'Build')-> Set[str]:
        return self._id

    def __str__(self: 'Build')-> str:
        string = ''
        for i, id_ in enumerate(self._id):
            string += '' if i == 0 else '.'
            string += id_
        return string

    def __gt__(self: 'Build',
               comparand: 'Build') -> bool:
        if len(self.id) > len(comparand.id):
            return True
        if len(self.id) < len(comparand.id):
            return False
        for i in range(len(self.id)):
            if self.id[i] > comparand.id[i]:
                return True
            if self.id[i] < comparand.id[i]:
                return False
        return False

    def __le__(self: 'Build',
               comparand: 'Build') -> bool:
        return not self.__gt__(comparand)

    def __eq__(self: 'Build',
               comparand: 'Build') -> bool:
        if len(self.id) != len(comparand.id):
            return False
        for i in range(len(self.id)):
            if self.id[i] != comparand.id[i]:
                return False
        return True

    def __ne__(self: 'Build',
               comparand: 'Build') -> bool:
        return not self.__eq__(comparand)

    def __lt__(self: 'Build',
               comparand: 'Build') -> bool:
        return not self.__gt__(comparand) and self.__ne__(comparand)

    def __ge__(self: 'Build',
               comparand: 'Build') -> bool:
        return self.__gt__(comparand) or self.__eq__(comparand)

    def __hash__(self: 'Build') -> int:
        return hash(self.id)


class SemanticVersion(object):
    """
    This is the internal representation of a semantic version.  It can create
    semantic version objects from external strings. i.e it has a semantic
    version factory, and can provide semantic version strings as an external
    string representation.
    """

    # This string contains the regular expression that defines the external
    # structure of a semantic version object.
    _pattern: Optional(re.Pattern) = None

    def __init__(self: 'SemanticVersion',
                 major: Counter = 0,
                 minor: Optional(Counter) = 0,
                 micro: Optional(Counter) = 0,
                 prerelease: Optional[PreRelease]=None,
                 build: Optional[Build]=None):
        self._major = major
        self._minor = minor
        self._micro = micro
        self._prerelease = PreRelease(prerelease) if prerelease else None
        self._build = Build(build) if build else None

    @property
    def major(self: 'SemanticVersion')-> Counter:
        return self._major

    @property
    def minor(self: 'SemanticVersion') -> Optional[Counter]:
        return self._minor

    @property
    def micro(self: 'SemanticVersion') -> Optional[Counter]:
        return self._micro

    @property
    def prerelease(self: 'SemanticVersion') -> Optional[PreRelease]:
        return self._prerelease

    @property
    def build(self: 'SemanticVersion') -> Optional[Build]:
        return self._build

    def __str__(self: 'SemanticVersion')->str:
        """
        Provides a semantic versioning valid string representation of the
        version.  It extends strict semantic versioning to allow versions with
        only major and minor components or with major components only as this
        represents the way semantic versioning is used in practice.

        :return: String representing the version
        :rtype: str
        """
        string = f'{self.major}'
        if self.minor is not None:
            string += f'.{self.minor}'
            if self.micro is not None:
                string += f'.{string.micro}'
                if self.prerelease is not None:
                    string += f'-{str(self.prerelease)}'
                    if self.build is not None:
                        string += f'+{self.build}'
        return string

    def __gt__(self: 'SemanticVersion',
               comparand: 'SemanticVersion') -> bool:
        # Test major version
        if self.major > comparand.major:
            return True
        if self.major < comparand.major:
            return False

        # Test minor version
        if self.minor is None:
            if comparand.minor is not None:
                return True
        elif comparand.minor is None:
            return False
        elif self.minor > comparand.minor:
            return True

        # Test micro version
        if self.micro is None:
            if comparand.micro is not None:
                return True
        elif comparand.micro is None:
            return False
        elif self.comparand > comparand.micro:
            return True

        # Test prerelease
        if self.prerelease is None:
            if comparand.prerelease is not None:
                return False
        else:
            if comparand.prerelease is None:
                return False
        return True if self.prerelease > comparand.prerelease else False
        

    def __le__(self: 'SemanticVersion',
               comparand: 'SemanticVersion') -> bool:
        not self.__gt__(comparand)

    def __eq__(self: 'SemanticVersion',
               comparand: 'SemanticVersion') -> bool:
        return True if (self.major == comparand.major and\
            self.minor == comparand.minor and\
            self.micro == comparand.micro and\
            self.prerelease == comparand.prerelease and\
            self.build == comparand.build) else False

    def __ne__(self: 'SemanticVersion',
               comparand: 'SemanticVersion') -> bool:
        return not self.__eq__(comparand)

    def __ge__(self,
               comparand: 'SemanticVeion'):
        return self.__gt__(comparand) or self.__eq__(comparand)

    def __lt__(self: 'SemanticVersion',
               comparand: 'SemanticVersion') -> bool:
        return not self.__ge__(comparand)

    def __hash__(self: 'SemanticVersion') -> int:
        return hash((self.major, self.minor, self.micro,
                     self.prerelease, self.build))

    @staticmethod
    def SemanticFactory(external: str) -> 'SemanticVersion':
        """
        Generates a SemanticVersion object from a string
        """
        if SemanticVersion._pattern is None:
            SemanticVersion._pattern = re.compile(r"""
# This regular expression pattern is based on the pattern suggested in the
# semantic version formal specification. It has been modified in the following
# ways:
# * Fix bugs.
# * Take advantage of the Python implementation of regular expressions.
# * Make more readable by taking advantage of the VERBOSE flag in Python to
#   put the expression on multiple lines and to include comments.
^  # Start of string
(?P<major> # The major group is mandatory.
          0|            # It can be zero
            [1-9][0-9]* # or a non-zero number with no leading zero.
)                       # End of the named group
(?:\.(?P<minor> # The minor named group is optional. If it is not present, the
                # micro group should not be present. This cannot be enforced
                # directly by regular expressions but can be checked in Python
                # code that examines the result of the regular expression
                # match.
               0|            # It can be zero
                 [1-9][0-9]* # or a non-zero number with no leading zero
     )                       # End of the named group
)                            # End of the optional group
(?:\.(?P<micro> # The micro named group is optional
               0|            # It can be zero
                 [1-9][0-9]* # or a non-zero number with no leading zero
     )                       # End of the named group
)                            # End of the optional group
(?:-(?P<prerelease> # The prerelease named group is optional.
                    # If it is present, it must contain at least one sub-group.
                    # The recognition of sub-groups is partially performed in
                    # Python code working on the results of the regular
                    # expression match.
                    # All sub-groups except the first are optional. Optional
                    # sub-groups are separated by a ".".
                    0|                  # The mandatory sub-group contents can
                                        # be zero or can be
                      [1-9][0-9]*       # a non-zero number with no leading
                                        # zero
                      | [0-9a-zA-Z]+    # or an alphanumeric character string.
                    (?:\.               # The start of an optional sub-group
                                        # with a "." used as a sub-group
                                        # separator.
                        0|              # The sub-group that may be zero
                          [1-9][0-9]    # or a non-zero number with no leading
                                        # zero.
                         | [0-9a-zA-Z]+ # or an alphanumeric character string.
                    )*                  # This sub-group may appear an
                                        # indefinite number of times.
    )                                   # End of the named group - prerelease.
)                                       # End of the optional group.
(?:\+(?P<buildmetadata> # The buildmetadata named group is optional.
                        # If it is present, it must contain at least one
                        # sub-group. The "." character is used as a sub-group
                        # separator.
                       [0-9a-zA-Z]+                   # This is the mandatory
                                                      # sub-group. It must
                                                      # contain an indefinite
                                                      # number of alphanumeric
                                                      # characters.
                                    (?:\.             # The start of an
                                                      # optional sub-group
                                         [0-9a-zA-Z]+ # If present, it must
                                                      # contain an indefinite
                                                      # number of alphanumeric
                                                      # characters.
                                    )                 # End of the buildmeta
                                                      # optional sub-group.
                                    *                 # Zero to an indefinite
                                                      # number of optional
                                                      # sub-groups may be
                                                      # present.
     )                                                # End of the named group
                                                      # - buildmeta.
)                                                     # End of the optional
                                                      # group.
$                                                     # End of version string
                                 """,                 # End of pattern
                                 re.VERBOSE)

        match = re.fullmatch(SemanticVersion._pattern,
                             external)
        if match is None:
            raise ValueError(f'String {external} does not describe'
                             ' a valid semantic version'
                             ' - it has an incorrect structure.')

        components = match.groupdict()
        if 'minor' not in components and 'micro' in components:
            raise ValueError('When the minor version is omitted, the micro'
                             ' version must also be omitted')

        mj = components.major
        mi = None if 'minor' not in components else components.minor
        mc = None if 'micro' not in components else components.micro
        pr = None if 'prerelease' not in components else components.prerelease
        bd = None if 'build' not in components else components.build
        return SemanticVersion(mj,
                               mi,
                               mc,
                               pr,
                               bd)
