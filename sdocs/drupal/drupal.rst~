Drupal
======

# Howto install Drupal


I Prerequisites
---------------

+ werbserver nginx and check php with info.php
+ databank mariadb or postgresql
+ phpmyadmin or phpPgAdmin
+ databank for drupal


II Installation
---------------

# Basic Steps

+ download drupal
+ move to target dir
+ extract drupal
+ configure drupal and set permissions
+ install drupal

# Advanced Steps

+ check webserver with info.php::

        <?php
        phpinfo();
        ?>

+ configure php (php.ini)::

        max_execution_time = 600
        max_input_time = 600
        mysql.connect_timeout = 600

+ configure mariadb (my-large.cnf) for translation import very important::

        innodb_flush_log_at_trx_commit = 2

+ extract drupal::
  
        tar xvzf drupal-7.34-DE.tar.gz

+ move drupal to target dir::

        mv drupal-x.x/* drupal-x.x/.htaccess ./
        For Drupal 7, also add:
        mv drupal-x.x/.gitignore ./
        
+ configure drupal::

        cp sites/default/default.settings.php sites/default/settings.php 
        chmod 664 sites/default/settings.php 
        chmod a+w sites/default
        cp drupal-7.34.de.po profiles/standard/translations
        
        # after installation
        chmod 644 sites/default/settings.php
        chmod 755 sites/default

+ configure cron::

        /usr/bin/curl -s $URL_A 


III Guides
----------

+ setup drupal: https://www.drupal.org/start
+ drupal installation: https://www.drupal.org/documentation/install
+ drupal with nginx: http://wiki.nginx.org/Drupal
+ translation-import: http://blog-das-oertchen.de/archive/201111/drupal-drupal-7-innodb-und-die-oberflaechenuebersetzung

IV Modules
----------

https://www.drupal.org/project/ctools
https://www.drupal.org/project/views
https://www.drupal.org/project/webform
https://www.drupal.org/project/panels



