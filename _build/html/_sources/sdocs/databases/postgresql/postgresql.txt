PostgreSQL
==========

# Howto Setup Postgresql

I Prerequisites
---------------

1. postgresql-5.1.tar.gz
2. privileged user only for sql-data
3. phpPgAdmin (manage tool)
4. barman (backup tool)


II Installation for Slackware
-----------------------------

+ use sbopkg

III Configuration
-----------------

1. create database

.. literalinclude::
        output/console-output-1

2. start the database
3. change user and group to what you set, edit rc.postgresql

.. literalinclude::
        output/console-output-2

IV Manage Database
------------------

+ phpPgAdmin

V Backup
--------

+ barman


.. phpPgAdmin_link


