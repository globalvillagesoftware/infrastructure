#############
Configuration
#############
Large parts of what is described here may not be implemented for some time. It
is described here to ensure that the actual implementation does not do things
that might interfere with the implementation of new features as resources
become available to do so.

**********
Objectives
**********
|gv| configuration should, at least, support open source software
development. Any extension of this support to commercial or governmental
environments will be a distant prospect.

Ultimately, configuration will support the development and use of a variety of
programs in the |gv| environment. In doing this, generality and the
possibilities of additional application areas should be kept in mind. At least
some of the developers will belong to organizations that have in-house needs
that differ from those of the |gv|.

**********************
What is configuration?
**********************
This is the collection of data that controls the operation of organizations
through to individuals to software programs that need data to determine how they
should operate. This data is computer based and should be accessible to all the
active elements involved in the development, running, and maintenance of
computer  programs. My thoughts started with computer program configuration but
it rapidly became apparent that this configuration information should support
the people involved in computer software and their activities. 

***********************
The Software Life-Cycle
***********************
A brief examination of the software development process as practiced by the
|gv| organization will be given here. Since the configuration must
support this process, it will help to uderstand a little of what the software
development process is all about. This is all written from the pespective of
open source software development,

Software Development
====================
Programs start with an idea. Computers get involved when individuals feel that
computers could help make the idea more accessible and usable. Since
communication is greatly facilitated by computers, they tend to get involved in
communication situations.

Roughly, the following steps take place during software development. The nature
of the steps varies somewhat, depending whether an individual or a group is
performing the development. The steps are not necessarily performed sequentially
but the entire process may be used iteratively, in a loop through the steps. It 
is not necessary to complete one step before starting the next. Many times, it
works better to loop over the whole process with each step resulting in a small
increment in functionality and a bigger one in the understanding of the nature
of the original idea.
 
Conception
----------
The initial step is getting an idea. Often the idea is a bit fuzzy. It is not
completely clear what the idea is and what are its' implications. I find the
following steps are helpful in trying to bring clarity to the idea. You might
only do one of them or you might do some selection of them, possibly
iteratively.

* Write down the concept in the form of a concepts document. |br| 
  This helps you to clarify the idea and gives you something concrete to work
  with when discussing the idea with other people. I find that the simple
  process of writing a concepts document helps too make the idea clear in my own
  mind. Writing the document also helps to recognize that an idea is very big
  and that it may be better to adopt a phased solution to the implementation of
  the idea.
  
  Never treat a concepts document as being cast in stone. It should be a living
  document that constantly changes as your understanding of the idea
  implications improves. Coomunicating changes in this document to stakeholders
  is obviously important.

* Develop a tentative project implementation plan. |br| 
  This is important for several reasons:

  * It is a great help in developing idea comprehension. |br| 
    Planning what you are going to do is a great help in understandng what is up.

  * It is an excellent communication mechanism. |br| 
    Most projects have stakeholders in one form or another. Keeping them
    informed about the plan and showing the progress in implementing the plan
    are valuable ways of communicating with stakeholders.

* Review the document and plan with stakeholders |br| 
  Keeping the project stakeholders in the loop is essential to successful
  project achievement.
 
Requirements
------------
Traditonally, requirements documents are massive tomes that describe what a
project should achieve, in minute detail. Sadly, they frequently bear little
resemblance to the delivered application.Reuirement documents are essential, but
to be useful, they must be cross-referenced to design documentation, concept
documentation, and possibly to implementation artifacts such as code or data to
ensure that the reqquirements document always reflects the status of the
implementation. An out-of-date requirements document loses a lot of its'
potential value.

If you adapt an iterative approach to project development, you will product many
requirements documents, one for each iteration. Or it might be a single
document with iteration based chapters.

Requirements can be the reference that is used when specifying acceptance tests
that verify that the application does what the stakeholders expect. These should
be defined, even in the absence of stakeholder. Always keep your potential
users in mind and treat them as virtual stakeholders.

Design
------
Here we work out how to implement the requirements. If you are using an
iterative approach, there may be many chapters to this document, one for each
iteration.

This work should be cross-referenced to the concept and requirements documents
to ensure that the document stays in synchronization with changing concept and
requirements. It also should link to implementation artifacts to ensure that the
implementation and the design are synchronized.

The |gv| Approach
^^^^^^^^^^^^^^^^^ 
Here we describe some early design choices. These are all subject to change as
implementation proceeds.

* Configuration data will be stored externally in the form of `JSON`. |br|
  `JSON`_ is a well established format that is widely used and is very
  compatible with the internal storage and processing that is required, since
  `Python`_ based implementations return translated `JSON` as a dictionary.  
  
Implementation
--------------

Testing
-------

Unit testing
^^^^^^^^^^^^

Functional testing
^^^^^^^^^^^^^^^^^^

Acceptance Testing
^^^^^^^^^^^^^^^^^^

Deployment
----------

Computer Operations
===================

Software Maintenance
====================

Project Management
==================

Iteration
---------

References
----------

*************************
Elements of Configuration
*************************

Constraints
===========

People
======

Organizations
-------------

Sites
-----

Individuals
-----------

Roles
^^^^^

Team Leader
"""""""""""

Developer
"""""""""

Tester
""""""

Operator
""""""""

Stakeholder
"""""""""""

Application
"""""""""""

Project
"""""""

Milestone
"""""""""

Plant
=====

Computers
---------

Management
==========

Operational Management
----------------------

System Management
-----------------

********************
Design Possibilities
********************

Concepts
========

Storage
=======

Data Formats
============

Internal
--------

External
--------

General
-------

Communication
=============
