PHPmyadmin
==========

# Howto Setup PHPmyadmin


I Prerequisites
---------------

+ databank mariadb or mysql
+ webserver with php enabled
+ phpmyadmin-4.2.11-noarch-1js.txz


II Installation
---------------

# Basic Steps

+ check mariadb
+ check webserver configuration with php (fastcgi, info.php)
+ set permissions of php sessions save path to webserver's user:group and 770 (grep session.save.path /etc/httpd/php.ini ; e.g. /var/lib/php)
+ install phpmyadmin
+ set permissions of phpmyadmin to webserver user:group (see nginx.conf, fastcgi.conf)
+ mkdir config && chmod o+rw && set permission according to the webserver
+ check setup url http://phpmyadmin/setup
 

III Configuration
-----------------

# basic steps

+ go to and follow the steps http://phpmyadmin/setup


# manual steps

1. cd phpMyAdmin
2. mkdir config                        # create directory for saving
3. chmod o+rw config                   # give it world writable permissions
4. cp config.inc.php config/           # copy current configuration for editing
5. chmod o+w config/config.inc.php     # give it world writable permissions
6. open http://phpmyadmin/setup/       # see nginx config
7. mv config/config.inc.php .          # move file to current directory
8. chmod o-rw config.inc.php           # remove world read and write permissions
9. open http://phpmyadmin/
10. login with root login and password
11. start adminstration


+ quick-setup: http://wiki.phpmyadmin.net/pma/Setup
+ quick-install: http://wiki.phpmyadmin.net/pma/Quick_Install
+ docs-config: http://docs.phpmyadmin.net/en/latest/config.html

