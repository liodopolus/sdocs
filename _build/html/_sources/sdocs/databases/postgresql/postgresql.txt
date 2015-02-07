PostgreSQL
==========

# Howto Setup Postgresql


I Prerequisites
---------------

1. postgresql-5.1.tar.gz
2. privileged user only for sql-data
3. phpPgAdmin (manage tool)
4. barman (optional backup tool)


II Installation for Slackware
-----------------------------

+ use sbopkg


III Configuration
-----------------

1. create user with username, give him a passwd and make sure to log in homedir /var/lib/pgsql/
2. create group with username or other
3. change permissions of /var/lib/pgsql/ to chown -R username:username
4. create database: su username -c "initdb -D /var/lib/pgsql/9.3/data --locale=de_DE.UTF-8 -A md5 -W"

.. literalinclude::
        output/console-output-1

5. change username and group in rc.postgresql
6. start the database: /etc/rc.d/rc.postgresql start

.. literalinclude::
        output/console-output-2


IV Manage Database
------------------

+ phpPgAdmin

# login with the privileged user above in phpPgAdmin


V Backuptools
-------------

+ pg_dump
+ barman


Postgresql Backup
-----------------

see: http://www.postgresql.org/docs/9.4/static/backup-dump.html

# dump db
pg_dump dbname > outfile

# reload db
psql dbname < infile


# dump large db
pg_dump dbname | gzip > filename.gz

# reload
gunzip -c filename.gz | psql dbname


.. phpPgAdmin_link

