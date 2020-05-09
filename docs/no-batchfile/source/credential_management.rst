#####################
Credential Management
#####################

********
Concepts
********
Managing credentials for authentication is a platform dependent exercise. Each
platform provides its' own type of service that allows one to store credentials
and retrieve them when necessary. Each service stores the credentials in an
encrypted form that means that an intruder, even if they can find the physical
place where the credentials are stored, cannot read them or make any use of
them.

The way that this service is offered is very platform dependent as are the
details of the capabilities offered by the service. This means that, if we want
to be platform independent, we must implement a platform independent interface
to platform dependent modules.

The functions needed, conceptually, are quite simple. We need to do the
following:

* Create credentials that are stored in the credential management system.
* Retrive the credentials when they must be presented to organizations that want
  to validate access to their services.
* Update the credential information as the actual credential information or
  information about the use of these credentials changes,
* Delete the credentials as they expire.

This process is known in the software industry as CRUD and it occurs in many
situations. We need to Create the credentials, Retrieve them, Update them, and
Delete them. Thus our platform independent system will offer these capabilities
and will interface with platform dependent components that will access
the actual operating system capabilities that implement these requirements.

************
Requirements
************
One of the biggest problems in dealing with authentication protocols is the
variety of authentication methods and associated data used. In |gv|
the following methods are most significant:

* Password authentication |br| 
  This is used to allow an entity to login securely to a site that needs to
  protect access to the information maintained by that site.
* Token authentication |br| 
  A token is a single document that encapsulates both the identity of an entity
  along with data that verifies that the entity is not counterfit. Tokens
  are used between entities and a single organization that issues them and are
  not useful for authentication to other organizations.
* Symmetric keys |br| 
* Asymetric keys |br| 
* Certificate authentication |br| 

The immediate need is for support for password authentication as that is the
most commonly used authetication mechanism and will be required to support the
authentication needed when many of the software process functions are automated.


******
Design
******

Initially, this support will be implemented for a Linux platform, but since the
|gv| is susposed to be platform neutral, it will also be implemented
for Windows as soon as possible to support the continued platform independence
of the |gv|.

**************
Implementation
**************

***
Use
***