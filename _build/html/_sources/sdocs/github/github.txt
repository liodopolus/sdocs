Github
======

.. |date| date::
.. |time| date:: %H:%M

# Howto Setup Github

I Prerequisites

1. git 
2. ssh
3. login on github


II Installation for Slackware

1. use slackpkg
2. use sbopkg
3. use SlackBuild scripts

III Configuration

# quick setup

create ssh key
add ssh key
create a repo in github


initialisize repo and push it to remote repo with same name
touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:liodopolus/scriptcol-current.git
git push -u origin master
(git remote add upstream git@github.com:liodopolus/scriptcol-current.git)

# simple howto

http://githowto.com/setup

# setup github
https://help.github.com/articles/set-up-git/

see too man git or man gittutorial::

        git config --global user.name "YOUR NAME" 
        git config --global user.email "YOUR EMAIL ADDRESS"

# create a repo

| https://help.github.com/articles/create-a-repo/
| https://help.github.com/articles/fork-a-repo/
| https://help.github.com/articles/be-social/

# git docs

http://git-scm.com/

# sync a fork

https://help.github.com/articles/syncing-a-fork/


# push a remote

        gitstatus
        git status

        first add
        git add *

        then commit
        git commit -m "Kommentar"

        then push
        git push

https://help.github.com/articles/pushing-to-a-remote/


