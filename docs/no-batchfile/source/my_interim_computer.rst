###################
My Interim Computer
###################

*********
Rationale
*********
This system will not last for long but it is an essential step towards where I
want to be. I want to write Python scripts to completely automate the creation
and maintenance of computer systems. This includes the installation
and maintenance of the software that I use, which may not come from the
supplier of my computer operating system. The result will be the creation of
an environment that will keep my entire computer system at the most up-to-date
level possible and make it trivial to restore it if the system somehow becomes
corrupted.

The other objective that I have is to be able to re-install an operating
system without losing any work I am doing. This supports the previous
objective since I will be able to re-install the software of my system at any
time without disrupting my workflow.

I want to implement a robust separation of system and user data. The principal
problem here is that the operating system replaces the home directory of the
user whenever the operating system is reinstalled. Obvious problem areas include
directories in the home directory, such as Documents and Downloads where a
person stores work-in-progress. The simple solution is to create symbolic links
to non-volatile directories. It may be necessary to copy data from these
directories to the non-volatile storage location before creating the symbolic
link. The biggest problem is that 3rd. party applications often store
configuration data in the user's home directory. This data gets destroyed when
the operating system is reinstalled and needs to be regenerated. In Ubuntu and
probably other Linux based systems, it is possible to specify where the home
directory is to be placed but the system still destroy what was there before. I
am still investigating how best to handle this problem. For example, it may be
possible to link to non-volatile configuration directories after installation of
the 3rd. party applications. The problem here is what should be done when some
of the configuration data should be updated when a new version of the
application is installed. I want to avoid individual solutions for each
application and eliminate the need to re-configure each application after
upgrading. This really should be handled by the authors of the 3rd. party app
but I have found none that have considered this aspect, in my experience. This
is a problem because apps often add new configuration items in new releases. For
the moment, I will just live with the problem until a general solution can be
found.

*******************
The System Contents
*******************
This system will be built manually. I will use this build as an opportunity to
completely document what I have done to customize my system as an aid to me in
determining the best way of automating system management. Three basic types of
system can be built, they are built and configured in different ways:

* Bare Metal |br|
  This is the traditional environment that communicates directly with the
  hardware of the computer system. When you get a new computer, you will need to
  construct a bare metal environment for it if you want to do anything unless it
  comes with an operating system pre-installed.
* Virtual Machine |br|
  These are run under the control of special software in bare metal environments
  that allows the simulation of bare metal environments so that operating
  environments can be tested without needing additional hardware to support new
  bare metal environments for testing. One of the big advantages of virtual
  machines is that they allow you to play with operating systems without fear of
  impacting the bare metal environment that supports them.
* Container Image |br|
  Containers are a new innovation in operating systems that provide many of the
  advantages of virtual machines with lower machine resource usage. They are
  implemented in the environment of the bare metal operating system. Containers
  are used primarily to run production servers in completely isolated
  environments but allow multiple containers to run on one physical machine,
  thus conserving physical machine resources. Containers run container images as
  their operating system software.

My System Configuration
=======================

Hardware Configuration
----------------------
* Machine   - Dell XPS 8700
* Processor - Intel Core I7-4770, 4 cores, 8 threads
* Memory    - 16 GB
* Disks

  * Kingston 200 GB SSD drive
  * Kingston 200 GB SSD drive
  * Western Digital 1 TB hard drive
  
* Peripherals

  * Microsoft LiveCam web camera - USB
  * Logitech keyboard - Wireless USB
  * Logitech mouse - Wireless USB  The keybord and mouse use independent
    wireless receivers on USB
  * RCA Monitor - connected via HDMI - 1920x1080 resolution
  * Wireless network port
  * DVD Drive
  * Cyber Acoustics headphone and microphone - USB

Software Configuration
----------------------

See :ref:`devtools`