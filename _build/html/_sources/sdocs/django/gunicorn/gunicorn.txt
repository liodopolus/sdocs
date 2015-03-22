Gunicorn
========

# howto setup and use gunicorn wsgi http server

http://gunicorn.org


I Prerequisites
---------------

+ python
+ nginx
+ postgresql
+ phpPgAdmin
+ gunicorn
+ django


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
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn

# nginx global config

.. literalinclude::
        nginx/nginx.conf

# nginx gunicorn config

.. literalinclude::
        nginx/gunicorn-localhost.conf

# here you can find startscripts at bottom if needed (see next point)
http://docs.gunicorn.org/en/latest/deploy.html


IV Running Djangoprojects
-------------------------

1. create a django project::
        django-admin.py startproject mysite

2. create a database in postgresql (more stable as other databases) use phpPgAdmin
3. change database setting in settings.py
4. sync database and create the superuser for the djangoproject::
        python manage.py syncdb
5. the most important ;-) start and test your application with gunicorn::
        gunicorn mysite.wsgi:application
see: https://docs.djangoproject.com/en/1.4/howto/deployment/wsgi/gunicorn/
6. create an app::
        python manage.py startapp [appname]
7. etc. 


