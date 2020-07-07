"""
Manage the application configuration for an application.

This class is only partially implemented, but allows the whole startup
infrastructure to be tested. It is intended that constructing the configuration
for an application will provide it with all the information needed to run. This
information can come from a variety of sources. The default implementation will
provide three sources but the software will allow any number of sources to be
defined. The sources are considered to be hierarchical so configuration
elements at a lower level will override the same elements from a higher level.
Configuration data will be persisted in
`JSON <https://www.json.org/json-en.html>`_ files which match closely in
structure with the dictionary structure used internally to hold configuration
data.

External configuration is stored in JSON files and is loaded into the computer
as a dictionary that contains the configuration data for the application. Third
party configuration modules must be capable of translating their information
into a JSOM compatible dictionary. Each source is responsible for the
maintenance of it's configuration data through a graphical program that has not
yet been developed.

Much of this data is stored in configuration files that are located via a
configuration index file that contains entries for the address of each
application. Configuration element names are grouped into functional groups
that work together. Groups may not be implemented in the initial configuration
module. The following groups are supported by this configuration and should be
supported by the user's interface module to any third party configuration
system:

* user |br| 
  This group contains personal information related to a specific user.
  Ultimately this information is supplied by the user or by the Human Resources
  department of am organization. This group is mandatory as it allows the
  tracking of problems related to the application.
  A user entry may specify one or more roles that a user fulfills in an
  organization.
* user roles |br| 
  These roles define what the user does within an organization. In many cases
  they actually define job titles. Roles are implemented as groups in their own
  right and provide a description of how the role relates to the organization.
  Roles include:

  * developer |br|
      This group contains a list of information related to the original
      developer(s) of this application. It may contain a list of links to
      group(s) that define each developer involved in the creation of this
      application. It contains information relating to the original developer
      of the application. It is used for problem tracking and is optional. It
      is only used when ???
    * team_developer|br| 
      This list of entries defines the members of the team that developed this
      application.

.. only:: development_administrator

    Created on Apr. 19, 2020
    
    @author: Jonathan Gossage

"""
#TODO: Complete documentation of the configuration process - Issue 1

from typing import Any, Optional, Dict, Mapping, List

from lib.parse_arguments import Arguments as _a

#import lib.version
#v = lib.version.Version

# Define the types of testing supported
unittests = 0x01
functionaltests = 0x02
integrationtests = 0x04
acceptancetests = 0x08
# Configuration item keys. These variables are for commonly used configuration
# elements. Others are organization or application specific and their keys will
# not appear here.

userid      = 'userid'
"""
*userid* is the operating system user identification of the user running the
program.
"""
username    = 'username'
""" *username* is the full name of the user running the program."""
uid         = 'uid'
""" *uid* is the numeric identifier of the user on Linux"""
gid         = 'gid'
""" *gid* is the numeric identifier of the user's primary group in Linux"""
debug       = 'debug'
"""
Run the program in `debugging <https://docs.python.org/3/library/debug.html>`_
mode in the Python interactive console or in other consoles such as
`Idle <https://docs.python.org/3/library/idle.html>`_ that support Python
debugging.
"""
testrun     = 'testrun'
"""
Run the program in `doctest <https://docs.python.org/3/library/doctest.html>`_
mode.
"""
profile     = 'profile'
"""
`Profile <https://docs.python.org/3/library/debug.html>`_ the python program.
"""
version     = 'version'
"""
Abbreviated program version. Global Village uses and supports
`semantic versioning <https://semver.org/>`_ ???
"""
release     = 'release'
"""
`Full <https://semver.org/>`_ program version.
"""
datecr      = 'datecr'
"""Date program was created."""
dateup      = 'dateup'
"""Date program was last updated."""
verbose     = 'verbose'
"""
Run program in verbose mode. This item can have values that range from 0-3
which controls how verbose the program is, i.e. how much debugging data is
provided. 0 is the most terse.
"""
pname     = 'pname'
"""The name of the program, as seen by the operating system"""

plid      = 'plid'
"""
Name of the operating system platform that is running.
"""
ppath       = 'ppath'
"""
Path to the directory that contains the platform specific modules for this
application.
"""
commandargs = 'commandargs'
"""
A list of the arguments passed from the command line when the application is
invoked. This is used in situations where the command line is emulated.
"""
umname      = 'umname'
"""Name of the application specific high-level module."""
umpkg       = 'umpkg'
"""Name of the package that contains the application module."""
umclass     = 'umclass'
"""
Name of the class that contains the high-level application specific code
"""
log         = 'log'
"""
The log to use throughout the application. This is a Python type.
"""
uac         = 'uac'
"""
The name of the application specific main-line function for this application
"""
cmdargs     = 'cmdargs'
"""
A list of arguments to be used in place of the command line. Mainly used for
debugging with tools like `unittest`."""
cmdfile      = 'cmdfile'
"""
The path to the file that is to be used for the configuration of this
application for a specific run.
"""
noupdate     = 'noupdate'
"""
Flag that supresses the update of a configuration value
"""
nologging    = 'nologging'
"""
Flag that suppresses the use of the gvLogging facility, leaving only the
ability to write messages to stderr.
"""
noargs       = 'noargs'
"""
Flag that suppresses the use of command line arguments
"""
noconfig     = 'noconfig'
"""
Flag that suppresses the use of configuration files leaving only the
configuration supplied by the Global Village
"""
logsys       = None
"""
The name of the module that invokes or supplies a third party gvLogging system
This module should be callable. We make use of the initialization and call
methods from this module.
"""
argsys       = None
"""
The name of the module that invokes or supplies a third party command line
argument processing system.
"""
test: Optional[int] = None
"""
Defines the kind of testing being done on this run
"""

#TODO: Update configuration.py with key names from cfg.data

class ArgDescriptor(object):
    """
    Describes how to define a command line override for a configuration entry.
    This is an attribute of the `CfgEntry` for a configuration item.
    If it has no value, the configuration item cannot be overridden fom the
    command line.
    """
    def __init__(self) -> None:
        pass


class CfgAdmin():
    """
    This class contains the administrative data associated with a configuration
    item. If it has no value, administrative ability for this configuration
    item will be limited.
    """
    def __init__(self) -> None:
        pass

class CfgEntry(object):
    """
    Encapsulates all the components of a configuration entry.
    """

#TODO: Expand definition to include ability to handle command line arguments
    def __init__(self,
                 name: str,
                 value: Any,
                 ad: Optional[ArgDescriptor]=None,
                 flags: int=0,
                 admin: Optional[CfgAdmin]=None) -> None:
        """
        :param str name:         Name of the configuration item
        :param Any value:        The value for the dictionary entry
        :param ArgDescriptor ad: The argparse definition. If present, the
                                 argument can be overridden from the command
                                 line.
        :param int flags:        Flags that control the usage of the argument
                                 They are independent of the administrative
                                 environment
        :param CfgAdmin admin:   Administrative data for this entry
        """ 
        self._name = name
        self._value = value
        self._ad    = ad
        self._flags = flags
        self._admin = admin

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self,
             name: str):
        self._name = name

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self,
              v: Any):
        self._value = v

    @property
    def argDes(self):
        return self._ad

    @argDes.setter
    def argDes(self,
              ad: ArgDescriptor):
        self._ad = ad

    @property
    def flags(self) -> int:
        return self.flags

    @flags.setter
    def flags(self,
              flags: int):
        self._flags = flags

    @property
    def admin(self):
        return self._admin

    @admin.setter
    def admin(self,
              admin: CfgAdmin):
        self._admin = admin


class Configuration(object):
    """
    classdocs TBA
    """

    def __init__(self: 'Configuration') -> None:
        """
        """

        self._cfg: Dict[str, CfgEntry] = {}
        # Gives default values for critical configuration that may not be
        # specified elsewhere
        default_cfg = ((debug, False), (profile, False), (noupdate, False),
                       (nologging, False), (noargs, False), (noconfig, True),
                       (cmdargs, None), (cmdfile, None), (version, 0.1),
                       (release, '0.1.0'), (verbose, 0), (uac, None),
                       (test, None))
        for k, v in default_cfg:
            if k not in self._cfg:
                self._cfg[k] = CfgEntry(k,
                                        v)

        # Load the master preliminary configuration

        # Add the application level initialization to the configuration
#        for c in init:
#            self.setMember(c)

        # Load up and merge the configuration file for this run
        # It cannot be done earlier because its' location may be specified on
        # the command line
        #TODO: Invoke the loading of the configuration files

        # Get the command line arguments if supported by this application

        if not self._cfg.get(noargs):
            self._cfg.update(_a().Parse())

    @property
    def cfg(self: 'Configuration') -> Dict[str, CfgEntry]:
        return self._cfg

    def setMember(self: 'Configuration',
                  key: str,
                  value: Any) -> None:
        """
        Sets an entry in the configuration given the key and value as separate
        entities. Default value are used for the ArgDescriptor and CfgAdmin
        properties of CfgEntry.
        """
        if key not in self._cfg:
            self._cfg[key] = CfgEntry(key,
                                      value)

    def add(self: 'Configuration',
            entry: Mapping[str, Any]) -> None:
        """
        Adds the contents of a Mapping to the configuration. The values are
        converted to CfgEntries.
        """
        for k, v in entry:
            if self._cfg.get(k) is None:
                raise(KeyError,
                      f'{k} is already in configuration - cannot add')
            self._cfg[k] = CfgEntry(v)

    def delete(self: 'Configuration',
               entry: CfgEntry):
        if isinstance(entry,
                      CfgEntry):
            if entry.key() not in self._cfg:  # Got an entry object
                raise(KeyError,
                      f'{entry.key} is not in configuration - cannot delete')
            else:
                    del self._cfg[entry.key()]
        else:  # Got a text key
            if entry.key() in self._cfg:
                raise(KeyError,
                      f'{entry} is not in configuration - cannot delete')
            else:
                del self._cfg[entry]

    def get(self: 'Configuration',
            key: str) -> Optional[Any]:
        return self._cfg.get(key)

    def len(self) -> int:
        return len(self._cfg)

    def _loadConfig(self,
                    cfg: List[str]) -> None:
        """
        Load the configuration data from disk

        :param List[str] cfg: A list containing the paths of the configuration
                              data files to be loaded.
        :returns:             Nothing. Everything is done as side-effects.
        """

        final_file = {}  # The consolidated configuration data
        for file in cfg:
            with open(file, 'r') as f:
                temp_file = self._cj.load(f)
                for ent in temp_file:  # Check for existing keys
                    #TODO: Handle updating of existing keys
                    # if not ent.key() in self._cfg or ent.key() in final_file:
                    final_file.update(ent)
        self._cfg.update(final_file)

    def __call__(self) -> Dict[str, CfgEntry]:
        """
        The configuration file resides in a platform specific location and can
        reside in a different place for testing so that test versions of the
        file can be used when testing. The name of the configuration file
        is passed as an argument to main(). For testing, the name of the
        testing file can be specified on the command line when the test is
        invoked.
        """
#TODO: Load configuration data from file

        # Return standard configuration augmented by the command line arguments
        return self._cfg
