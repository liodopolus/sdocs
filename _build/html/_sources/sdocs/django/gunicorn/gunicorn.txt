Gunicorn
========

# howto setup and use gunicorn wsgi http server

http://gunicorn.org


I Prerequisites
---------------

+ python
+ nginx
+ gunicorn
+ django (optional)


II Quickstart
--------------

http://gunicorn.org/#quickstart

.. literalinclude::
        output/console-output

# howto start apps (hello world)

.. literalinclude::
        hello-world/readme

II Configuration
----------------

# howto configure nginx for gunicorn
http://docs.gunicorn.org/en/latest/deploy.html

# nginx global config

.. literalinclude::
        nginx/nginx.conf

# nginx gunicorn config

.. literalinclude::
        nginx/gunicorn-localhost.conf


