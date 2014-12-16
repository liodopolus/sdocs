Sound
=====

.. |date| date::
.. |time| date:: %H:%M


# Howto Setup Sound

I Prerequisites
---------------

+ alsa


II Installation for Slackware
-----------------------------

+ use slackpkg
+ use sbopkg
+ use SlackBuild scripts


III Configuration
-----------------

# quick setup

+ lsmod | grep snd (check if snd_hda_intel is loaded)
+ aplay -l (check sound devices)
+ cat /proc/asound/card*/codec* | grep Codec
+ alsamixer
+ alsactl store
+ kde system setup multimedia


# setup sound [#f1]_ 

+ http://docs.slackware.com/howtos:hardware:audio_and_snd-hda-intel 


# global sound configuration  ::

        alsamixer
        alsactl store

# special sound configuration ::

        echo "options snd-hda-intel model=auto" > /etc/modprobe.d/snd-hda-intel.conf


# output of aplay -l ::

        **** List of PLAYBACK Hardware Devices ****
        card 0: PCH [HDA Intel PCH], device 0: CONEXANT Analog [CONEXANT Analog]
        Subdevices: 1/1
        Subdevice #0: subdevice #0
        card 0: PCH [HDA Intel PCH], device 1: Conexant Digital [Conexant Digital]
        Subdevices: 1/1
        Subdevice #0: subdevice #0
        card 0: PCH [HDA Intel PCH], device 3: HDMI 0 [HDMI 0]
        Subdevices: 1/1
        Subdevice #0: subdevice #0

# output of cat /proc/asound/card*/codec* | grep Codec ::

        Codec: Conexant CX20588
        Codec: Intel CougarPoint HDMI


.. rubric:: footnotes

.. [#f1] see too: /etc/modprobe.d/sound.conf


