Mount
=====

# a quick start guide


I Prerequisites
---------------

1. mount
2. udisk


II Automount
------------

see: https://help.ubuntu.com/community/Mount/USB
see: https://help.ubuntu.com/community/RenameUSBDrive

# first umount all partions!

+ use blkid to dump partitions::
        blkid


NTFS
^^^^

+ check labeling of ntfs partions::
        ntfslabel /dev/sdc2

+ change label of ntfs partions::
        ntfslabel /dev/sdc? label


XFS
^^^

+ check labeling of xfs partions::
        xfs_admin -l /dev/sdc1

+ change label of xfs partions::
        xfs_admin -L label /dev/sdc1



