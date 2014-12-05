Github
======

.. |date| date::
.. |time| date:: %H:%M


# Howto Setup Github

I Prerequisites
---------------

+ git 
+ ssh
+ login on github


II Installation for Slackware
-----------------------------

+ use slackpkg
+ use sbopkg
+ use SlackBuild scripts


III Configuration
-----------------

# quick setup

+ create ssh key
+ add ssh key
+ create a repo in github
+ push your changes to your repo


# setup git [#f1]_ 

+ https://help.github.com/articles/set-up-git/


# global git configuration  ::

        git config --global user.name "YOUR NAME" 
        git config --global user.email "YOUR EMAIL ADDRESS"


# initialisize repo and push it to remote repo with same name ::

        cd repo
        touch README.md
        git init
        git add README.md
        git commit -m "first commit"
        git remote add origin git@github.com:githubuser/repo.git
        git push -u origin master


IV How to use it
----------------

# simple howtos

+ http://githowto.com/setup
+ http://gitreal.codeschool.com/levels/1


V Other Dokumentation
---------------------

# create a repo

+ https://help.github.com/articles/create-a-repo/
+ https://help.github.com/articles/fork-a-repo/
+ https://help.github.com/articles/be-social/

# sync a fork

+ https://help.github.com/articles/syncing-a-fork/
+ https://help.github.com/articles/pushing-to-a-remote/

# git docs

+ http://git-scm.com/


VI Use the Repo
---------------

# e.g. fork sphinx docs on readthedocs

+ https://readthedocs.org/


.. rubric:: footnotes

.. [#f1] see too: man git or man gittutorial


