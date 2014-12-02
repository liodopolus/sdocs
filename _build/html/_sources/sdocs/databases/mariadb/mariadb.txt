MariaDB
=======

# Howto Setup MariaDB

I Prerequisites


1. mariadb-5.5.40-x86_64-2.txz 
2. privileged user only for sql-data, mostly mysql


II Installation for Slackware

1. use slackpkg
2. use sbopkg
3. use SlackBuild scripts

III Configuration

Howto: http://docs.slackware.com/howtos:databases:install_mariadb_on_slackware

        1. mysql_install_db --user=mysql
        2. chown -R mysql.mysql /var/lib/mysql
        3. chown 755 /etc/rc.d/rc.mysqld
        4. /etc/rc.d/rc.mysqld start
        5. mysqladmin -u root password 'NEW_PASSWORD'
        6. use phpmyadmin to manage databases

.. literalinclude::
        output/console-output

