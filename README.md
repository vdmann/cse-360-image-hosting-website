cse-360-image-hosting-website
=============================
Image upload CSC-360 Visitnna Dee Mann, Derek Norman, and Dakota Nunez

Here is a list of dependencies if there are problems be sure to use "sudo pip install" we used a virtual env in ubuntu 14.04 using "source bin/activate" to start the environment

Django==1.6.1
MySQL-python==1.2.5
Pillow==2.6.1
South==1.0.1
argparse==1.2.2
coverage==3.7.1
django-ajax==2.2.12
django-annoying==0.8.0
django-appconf==0.6
django-imagekit==3.2.4
django-model-utils==2.2
django-storages==1.1.8
extras==0.0.3
fuzzywuzzy==0.4.0
lettuce==0.2.20
nose==1.3.4
pilkit==1.1.12
pysqlite==2.6.3
python-memcached==1.53
python-mimeparse==0.1.4
python-subunit==1.0.0
python-varnish==0.2.1
pytz==2014.7
selenium==2.44.0
six==1.8.0
sure==1.2.7
testtools==1.4.0
uWSGI==2.1
unittest2==0.8.0
virtualenv==1.11.6
wsgiref==0.1.2

=============================
Modifying the Database

To delete the db.sqlite database "cd" into the "src" folder directory in terminal then "ls" which will list out files and folders in the the directory, make sure that "db.sqlite3" is in the directory then "sudo rm db.sqlite3" to remove it. To create a new database schema simply execute "python manage.py syncdb". This will require you to create a superuser(admin) in terminal.

=============================
Is this the key for rackspace cloud?
4dc97a384c2ead36f934d71fe15019b0338b049a
