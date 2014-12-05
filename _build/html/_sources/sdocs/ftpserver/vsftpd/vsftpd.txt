Vsftpd
======

# configuration of vsftpd

http://www.basicconfig.com/linuxnetwork/ftp_server#check-vsftpd
http://wiki.ubuntuusers.de/vsftpd


.. literalinclude::
        config/vsftpd.conf

# restart the process

root@gamma:~# /etc/rc.d/rc.inetd restart 
Starting Internet super-server daemon:  /usr/sbin/inetd


# customize the login with vsftpd.banner_file


.. literalinclude::
        config/vsftpd.banner_file


# allow user who are permitted to login with vsftpd.user_list


.. literalinclude::
        config/vsftpd.user_list


# allow user who are login with chroot in a jail with vsftpd.chroot_list


.. literalinclude::
        config/vsftpd.chroot_list


