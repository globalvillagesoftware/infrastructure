#####################
Use of *Git* Branches
#####################

**********
Background
**********
The fundamental reason for the existence of `branches` in *Git* is to provide a
mechanism to ensure that development and maintenance work does not corrupt the
deployed software. A branch is essentially a copy of the core data in the
repository. You can develop and test new functionality or do maintenance in a
branch without impacting the integrity of the core code and data that make up the
current version of the delivered application. Once the new functionality has
been developed and tested, it is ready for integration into the main
application. This is done through a new process called `merging` that puts the
new code and data into the main code for the application. Note that this does
not happen until all code has completed development and been tested. Testing
checks both the existing and the new functionality. This ensures that the new
code does not break any existing functionality.

***************
Use of Branches
***************
Branches in *Git* each have a name which can be anything that you want.
Conventions, however, have developed over time. The production application code
is normally kept in a branch called `master`. This is is the default branch
within *Git*. Most organizations create a branch called `development`. The
purpose of this branch is to hold all code that will become part of the next
release. The same problem exists during the development cycle as does during
production. With potentially many people working on the next release at the same
time, it becomes necessary to deal with the problem of developers interfering
with the work of other developers.

Topic Branches
--------------
This is solved by creating additional branches, called `topic` branches, on top
of the `development` branch. Each individual piece of functionality or
maintenances is given its' own `topic` branch which is where work on the feature
takes place. When development and testing on a `topic` branch is complete, the
`topic` branch is merged into the `development` branch and so becomes part
of the content of the next application release. When the `topic` branch has been
sucessfully merged, it is put to bed and is no longer used. The productive life
of a `topic` branch is that of the feature that is being developed only. `Topic`
branches normally stay around after the feature is completely developed, but
they are kept for historical reasons only and are no longer used.

Release Management
------------------
A release happens when a new version of the application software is made
available to the application users. These releases always come from the `master`
branch. The point at which the new release is successfully accomplished is given
a `tag` within *Git* which is a named point in the history of the main branch
and allows for the retrieval of the code that was associated with a particular
release.

Thus, over time, the `master` branch will acquire a series of `tags` that will
identify each release of the application software. The `development` branch is
associated with a particular release and the release version number will form
part of the name of the `development` branch. Once a release is made,
the `development` branch is no longer used and a new `development` branch is
created for the next release. This cycle repeats adinfinitum.

Patch Branches
--------------
Once a release is put into production and starts being used, problems are
encountered and reported. Fixing most of these problems can be deferred to the
next scheduled release and the work needed to fix them can become part of the
normal development cycle for the next release. However, it may turn out that
some problems  are critical and must be addressed immediately. These problems
do not fall into the normal pattern of development and must be handled in a
special way.

Special branches called `patch` branches are created from the `HEAD` of the
current `master` branch. This is done to ensure that there are no major
breakages between the `patch` and the `master` branches. It also potentially
shortens the time needed to develop a `patch` release since no attention is paid
to the next release. Once the patch has been fully tested, a new `patch` release
of the application can be made. Work on the `patch` is not complete yet. It
still needs to be checked against the current `development` branch to ensure
that it does not affect the next release and that it continues to supply the
needed `patch` functionality. Note that `tags` are created on the `master`
branch for each `patch` release.

The process continues by done by merging the `patch` branch with the current
`development` branch and then testing that the `patch` still works and that the
`development` branch is not corrupted in any way.
