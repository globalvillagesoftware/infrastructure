"""
Helper functions for the *Global Village* environment

.. only:: development_administrator

    Created on May 7, 2020
    
    @author: Jonathan Gossage
"""

import sys
import pathlib

PLATFORM = None


def validate_platform():
    """Check that we are running on a supported platform"""
    global PLATFORM
    PLATFORM = sys.platform
    if not PLATFORM.startswith('linux') and not PLATFORM.startswith('windows'):
        raise GlobalVillageException(f'{PLATFORM}'
                                     ' is not a supported platform')
    return PLATFORM


class GlobalVillageException(Exception):
    """General exception raised by the Global Village software"""

    def __init__(self, msg):
        super(msg)


class Helper():
    """Contains helper classes used throughout the Global Village codebase"""

    def __init__(self, url='https://github.com/globalvillagesoftware'):
        self._giturl = url
        self._platform = validate_platform()

    @property
    def url(self):
        """
        Gives the URL to the remote site containing repositories.
        Temporary fix until the characteristics of a remote site are stored in
        the configuration data. Only works for GitHub.
        """
        return self._giturl

    def prepare_url(self, url):
        """Prepare a URL for use on the Internet"""
        pass

    def repository_exists_on_Github(self, web_path):
        """
        Test if a copy of the repository exists on GitHub.
        First validate the web address and then see if GitHub has the
        repository

        :param str web_path: URL of the repository whose existence is to be
                             verified
        """
        return False  # Not implemented yet

    def clone_repository_via_api(self, path, reponame):
        """Clone a repository from GitHub"""
        pass

    def clone_repo_copy(self, path):
        """Clone a copy of a repository"""
        pass

    def clone_repo(self, path):
        """Clone a non-existent repo"""
        pass

    def get_repo(self, path):
        """
        Get the path and name of a local repository from a path

        :param path str: Path to the repostory
        :return: the path to the directory that contains the repository and
                 the name of the directory that contains the repository as a
                 tuple
        :rtype: tuple(str, str)
        """

        p = pathlib.PurePath(path)
        return (str(p.parent), str(p.name))

    def create_repository_on_GitHub(self, reponame):
        """Create a repository on GitHub using the GitHub API"""
        pass
