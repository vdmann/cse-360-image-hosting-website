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
    'django.contrib.sites',
    # my apps
    # 'signups',
    'drinker',
    'dragdrop',
    'south', # Only if you're relying on South for migrations
    'imagekit',
    'annoying',
    # using ajax, this can possibly make things slightly easier
    # with images
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
# 



SESSION_ENGINE = "django.contrib.sessions.backends.cached_db" 

# using file-based sessions
# can we use this to retrieve the user's session information in which we can use 
# for our string_builder feature?
# SESSION_ENGINE = "django.contrib.sessions.backends.file"
SESSION_FILE_PATH = ""



# Goes through MIDDLEWARE_CLASSES first then looks for "views" and looks for 
# INSTALLED_APPS
MIDDLEWARE_CLASSES = (
    # for authentication in web requests
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # for authentication in web requests
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

# where URL's are handles in each part 
ROOT_URLCONF = 'mvp_landing.urls'

WSGI_APPLICATION = 'mvp_landing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        # sqlite3 automatically generates tables using these two statements
        # not reccommended for live deployment
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'USER':'',
        #'PASSWORD':'', 
        #'HOST':'',
        #'PORT':'',
            
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

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# what is rendered by the browser, not so much Django
STATIC_URL = '/static/'

# this is for photologue (not working)
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loarder',
# )

# this is for photologue
# from photologue import PHOTOLOGUE_APP_DIR

# setting our template location
# note this is a tuple
TEMPLATE_DIRS = (
    
    # this joins the path of the folder that is 1 up the base directory
    # it will look for static and under static it will look for templates 
    os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),
    
    # this is for photologue
    # PHOTOLOGUE_APP_DIR
    
    # Replaces the normal templates with the templates that used to come with 
    # Photologue 2.X. Use these if you have an existing project that extends 
    # these old-style templates.
    # os.path.join(PHOTOLOGUE_TEMPLATE_DIR, 'contrib/old_style_templates'),

    # this is a reference:
    # '/home/dee-mann/Desktop/skillshare/static/templates/',

)



if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
    
    # where pictures are stored
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
    
    # a tuple that collects CSS and JavaScript files
    # useful for production and collecting static files.
    # note that this is a tuple. This loads the static files
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



# this is for Django's memcache
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': [
#             '172.19.26.240:11211',
#             '172.19.26.242:11212',
#             '172.19.26.244:11213',
#         ]
#     }
# }

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
VANRISH_WATCHED_MODELS = 'auth.user','drinker.Drinker'
VARNISH_MANAGEMENT_ADDRS = 'server1:6082', 'server2:6082'