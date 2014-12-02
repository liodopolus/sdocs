PHPmyadmin
==========


# Howto Setup PHPmyadmin

I Prerequisites

1. phpmyadmin-4.2.11-noarch-1js.txz


II Installation for Slackware

1. use slackpkg
2. use sbopkg
3. use SlackBuild scripts

III Configuration

Setup: http://wiki.phpmyadmin.net/pma/Setup
Quick-Install: http://wiki.phpmyadmin.net/pma/Quick_Install

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


