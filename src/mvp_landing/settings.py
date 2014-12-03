"""
Django settings for mvp_landing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


# gets the file where were at of the directory name of that file, which is "src"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# this is a reference:
# BASE_DIR = '/home/dee-mann/Desktop/skillshare/src'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'faiik0n61x)+=8m&z-o())ifijj(mii31+28_1xg_cb%td1*%3'

# SECURITY WARNING: don't run with debug turned on in production!
# for when we want to find errors.
DEBUG = True 

# not sure if I actually need this line of code for the MySQL database
TEST = True

TEMPLATE_DEBUG = DEBUG
#TEMPLATE_DEBUG = True

# EXAMPLE:
# when...
#
#DEBUG = False
#TEMPLATE_DEBUG = False
#
# enable...
#
# this ensures security only on specific domains
# ALLOWED_HOSTS = ['www.yourwebsite.com']

ALLOWED_HOSTS = []

# provide our get_profile()
# provides authentication to the Django backend
AUTH_PROFILE_MODULE = 'drinker.Drinker'
# this is for the dragdrop images
# AUTH_USER_MODEL = 'auth.User'


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    # User authentication in Django
    # The permission model in django.contrib.auth depends on django.contrib.contenttypes.
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     # this is for django-photologue
    # 'django.contrib.sites',
    # 'signups',
    'drinker',
    'dragdrop',
    'south', # Only if you're relying on South for migrations
    'imagekit',
    'annoying',
    # 'django_ajax',
    'filter',
    'storages',
    # 'varnishapp',
    'lettuce.django',
)

# for PHP
# PHP_CGI = '/usr/local/bin/php-cgi'

# this is for django's ajax upload feature

# Enabling the sites framework
SITE_ID = 1

# using South migrations for photologue
SOUTH_MIGRATION_MODULES = {
    # 'photologue': 'photologue.south_migrations',
}



# cache configuration to store our user's session data
# remember we want a persistent session so this allows the user to re-access the 
# website with images loaded/displayed at login
# 
# TAKEN FROM THE DJANGO DOCUMENTATION:
# This uses a write through cache  every write to the cache will also be 
# written to the database. Session reads only use the database if the data is 
# not already in the cache.
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db" 
# SESSION_ENGINE = "django.contrib.sessions.backends.file"
SESSION_FILE_PATH = ""


MIDDLEWARE_CLASSES = (
    # adding per-site caching, which caches the whole website
    # for caching, this has to be the first in the list
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # for caching, this has to be in the last of the list
    'django.middleware.cache.FetchFromCacheMiddleware',
)

# caches for 60 seconds?
CACHE_MIDDLEWARE_SECONDS = 600
# CACHE_MIDDLEWARE_ALIAS

# where URL's are handles in each part 
ROOT_URLCONF = 'mvp_landing.urls'

WSGI_APPLICATION = 'mvp_landing.wsgi.application'

DATABASES = {
    'default': {
        # sqlite3 automatically generates tables using these two statements
        # not reccommended for live deployment
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER':'',
        'PASSWORD':'', 
        'HOST':'',
        'PORT':'',
            
        # were using MySQL instead
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'mydb',
        # 'USER': 'mydb_user',
        # 'PASSWORD': 'your_password',
        # 'HOST': '',   # Or an IP Address that your DB is hosted on
        # 'PORT': '',
        
        # this is for PostgreSQL
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': 'django_db',                      
        # 'USER': 'django_login',                   
        # 'PASSWORD': 'your_password',              
        # 'HOST': 'localhost',                      
        # 'PORT': '5432', 
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'


TEMPLATE_DIRS = (    
    os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),
)


if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
    
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")

    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), 'static', 'static'),
    )


# this is for Rackspace for when we deploy it on the cloud
# CLOUDFILES_USERNAME = 'pnorman'
# CLOUDFILES_API_KEY = 'dcaee6c3f989850ceeb61eaa8ea15637'
# CLOUDFILES_CONTAINER = 'imageproject'
# DEFAULT_FILE_STORAGE = 'backends.mosso.CloudFilesStorage'

# Optional - use SSL, requires HTTPS
# CLOUDFILES_SSL = True


# OUTPUT FROM TERMINAL WHEN MEMCACHED IS ENABLED
# [28/Nov/2014 01:00:09] code 400, message Bad HTTP/0.9 request type ('get')
# [28/Nov/2014 01:00:09] "get :1:views.decorators.cache.cache_header..6666cd76f96956469e7be39d750cc7d9.en-us.UTC" 400 -
# [28/Nov/2014 01:00:09] code 400, message Bad request syntax ('set :1:views.decorators.cache.cache_header..6666cd76f96956469e7be39d750cc7d9.en-us.UTC 1 600 25')
# [28/Nov/2014 01:00:09] "set :1:views.decorators.cache.cache_header..6666cd76f96956469e7be39d750cc7d9.en-us.UTC 1 600 25" 400 -
# [28/Nov/2014 01:00:09] "GET / HTTP/1.1" 200 7159
# [28/Nov/2014 01:00:09] "GET /static/css/custom.css HTTP/1.1" 304 0
# [28/Nov/2014 01:00:09] code 400, message Bad HTTP/0.9 request type ('get')
# [28/Nov/2014 01:00:09] "get :1:views.decorators.cache.cache_header..35a63c8a85b1279a0f991ce8828fb9d9.en-us.UTC" 400 -

# this is for Django's memcache
CACHE_BACKEND = 'memcached://127.0.0.1:8000/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
            '127.0.0.1:8000',
            # '172.19.26.242:11212',
            # '172.19.26.244:11213',
        ]
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'cache_table',
#     }
# }

# In this example, a filesystem backend is being configured with a timeout of 60 
# seconds, and a maximum capacity of 1000 items:
# 
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache',
#         'TIMEOUT': 60,
#         'OPTIONS': {
#             'MAX_ENTRIES': 1000
#         }
#     }
# }


# this is for Varnish caching for HTTP acceleration
# VANRISH_WATCHED_MODELS = 'auth.user','drinker.Drinker'
# VARNISH_MANAGEMENT_ADDRS = 'server1:6082', 'server2:6082'



# SSH'ing into Rackspace
# ssh dee@166.78.144.71
# password is 123



# ssh root@166.78.144.71
# 5GfMh2J9kHh3

# server2
# 166.78.147.191:8000
# ssh root@166.78.147.191
# pdye8ysbsTW3 -new
# VtSfPTnY3X9e

# load bal
# 104.130.251.238