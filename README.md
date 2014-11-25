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

To delete the db.sqlite3 database "cd" into the "src" folder directory in terminal then "ls" which will list out files and folders in the the directory, make sure that "db.sqlite3" is in the directory then "sudo rm db.sqlite3" to remove it. To create a new database schema simply execute "python manage.py syncdb". This will require you to create a superuser(admin) in terminal.

=============================
Registered Users

The db.sqlite3 provides an already registered superuser and a regular user for the the superuser password and login information it is "dee-mann" for login and "123" for the password. For our regular user login, the login information is "123" and password is "123"

=============================
Code Coverage Report

To see code coverage from testing, by typing this:

"coverage run manage.py test -v 2"

you will get to see how much code you've tested

this command:

"coverage html"

creates a htmlcov folder in the src folder so you can actually look at the list of nice reports on things that were tested into a html template so when you click on index.html you get to see all the tests and the % covered
if you go into the individual things that were tested for example drinker_files.html it'll display the whole code block and with syntax highlighted indicated which lines of code that skipped the tests. There usually represented in red

"cd" into src->htmlcov to find html test code coverage reports on individual apps.


=============================
DISCLAIMER:

Testing was done on Firefox using Selenium

User functionality without Selenium testing should be done only on Chrome!

When running "python manage.py test", there will be a total of 10 tests. By the second/third test, it tests the browser functionality running the window sideways. If that test hangs simply drag your testing window sideways in order for testing to continue. This will output an error in terminal and on the report below.

test_login_user_navigation_bar_test_admin (drinker.tests.LoginUserNavigationBarTestAdmin) ... ERROR
test_login_user_navigation_bar_test_user (drinker.tests.LoginUserNavigationBarTestUser) ... ERROR

=============================
Is this the key for rackspace cloud?
4dc97a384c2ead36f934d71fe15019b0338b049a
