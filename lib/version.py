"""
Created on Apr. 26, 2020

Implements `semantic versioning <https://semver.org/>`_. It implements the
entire specification.

@author: Jonathan Gossage
"""

class Prerelease(object):
    """
    Implements the prerelease component of a semantic based version
    """

class Build(object):
    """
    Implements the build name component of a semantic based version.
    """

class Version(object):
    """
    This is the internal representation of a semantic version. It can create
    semantic version objects from external strings and can provide semantic 
    version string represented as an external strring.
    """

    def __init__(self, major, minor, patch=None, prerelease=None ):
        self._major = major
        self._minor = minor
        self._patch = patch
        self._prerelease = prerelease

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value

    @property
    def minor(self):
        return self._minor

    @minor.setter
    def minor(self, value):
        self._minor = value

    @property
    def patch(self):
        return self._patch
        
    @patch.setter
    def patch(self, value):
        self._minor = value

    @property
    def prerelease(self):
        return self._prerelease

    @prerelease.setter
    def prerelease(self, value: Prerelease ):
        self._prerelease = value

    def __str__(self):
        """
        Provides a semantic versioning valid string representation of the
        version.
            
        :return: String representing the version
        :rtype: str
        """
        if self.patch() is not None and self.prerelease() is not None:
            return\
            f'{self.major()}.{self.minor()}.{self.patch()}-{self.prerelease()}'
        elif self.patch() is not None:
            return f'{self.major()}.{self.minor()}.{self.patch()}'
        else:
            return f'{self.major()}.{self.minor()}'

    def precedence(self, comparand ):
        """
        Determines the precedence between two version numbers.
        One is this object and the other is another version object.
            
        :param Version comparand: Version to compare against this version
        :return: False indicates comparand <= this version
        :rtype: bool
        """

        if self.major > comparand.major:
            return True
        if self.minor > comparand.minor:
            return True
        if self.patch > comparand.patch:
            return True
        return False  # There is no precedence

    def _StoreComponents( self, external):
        """
        Breaks down the string variant of a version into the individual
        components, validating them along the way.
        """
        pass

