"""
Control components of a workflow that can work in parallel with each other.

.. only:: development_administrator

    Created on Jun. 20, 2020
    
    @author: Jonathan Gossage
"""

#__all__ = ['Workflow', 'Component', 'ResourceProvider', 'Resource', 'Process',
#           'Module']

from importlib import import_module as _im
from typing import Optional

from lib.gvLogging import Logging as _L


class Workflow():
    """
    Collection of components needed to accomplish a job.

    A workflow my contain a single component or multiple components that are
    connected in different ways.
    """
    def __init__(self):
        _L.warning(
            'gvMmultiprocessing - The Workflow class is not implemented')
        super()


class Component():
    """
    Base class for any items that may be atomic components of a workflow

    These include processes and *Python* modules that may run in parallel with
    the workflow controller that created them.

    Components need resources to carry out their function and can be connected
    in various ways to form a network of components.

    Components also contain ports. They are the points in an application
    through which resources can be accessed. Ports can access file objects such
    as stderr, stdout or some other file object or they can be ResourceProvider
    objects that provide access to an underlying resource. The set of ports for
    a component define the set of Resources used by the component.
    """
    def __init__(self) -> None:
        self._resources = {}
        self._ports = {}

    def addResource(self):
        """
        Adds a resource to the component
        """
        pass


class Resource():
    """
    A resource is something that a component needs to perform its work.

    Examples could include files, database records or pieces of information
    that may be generated by other components. Resources such as existing files
    may be iterable or they may be atomic.

    Normally, each Resource has a single ResourceProvider, but it may contain
    several in cases where the resource may come from multiple sources.

    Resources may be immutable or they may support changing the content of the
    resource. A Resource object will guarantee that the synchronization
    primitives such as locks have been established and that integrity of the
    resource will be maintained during use.

    Resources will be obtained and released. This capability helps ensure that
    the integrity of the resource is maintained by delimiting the time period
    during which a resource is used by a particular requester.

    Resources may implement resource protection themselves or they may delegate
    to the underlying implementation such as a file. The purpose of a Resource
    instance is to insulate the implementation of the resource from the rest
    of the system.

    """
    def __init__(self, name, value) -> None:
        _L.warning('gvMultiprocessing - The Resource'
                   ' class is not implemented')


class ResourceProvider():
    """
    A resource provider encapsulates the method of accessing a resource.

    ResourceProviders may encapsulate files, queries, databases or anything
    that can supply resources to a component.
    ResourceProviders provide a way of encapsulating and hiding the method of
    access to a particular resource.
    """
    def __init__(self,
                 Resource: Optional[Resource]=None) -> None:
        _L.warning('gvMultiprocessing - The ResourceProvider'
                   ' class is not implemented')
        self._resource = Resource

    @property
    def resource(self) -> Optional[Resource]:
        return self.resource

    @resource.setter
    def resource(self,
                 res: Resource) -> None:
        self_resource = res


class Process(Component):
    """
A component of a workflow that is handled by the operating system.

Such a component might be a *Unix* command such as `ls -al` or a graphical
application such as *Gimp*. It functions as a converter between a component and
the driver that controls the running of this component
    """
    def __init__(self,
                 driver: str="subprocess") -> None:
        super()
        _im(driver)  # Import the driver module


class Module(Component):
    """
    A *Python* module or class that can be a component of a workflow.

    """
    def __init__(self) -> None:
        _L.warning('gvMultiprocessing - The Module'
                   ' class is not implemented')
        super()
