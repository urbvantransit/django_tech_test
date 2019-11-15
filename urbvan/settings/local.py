# coding: utf8
from .base import os, BASE_DIR


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'db_write': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_write.sqlite3'),
    },
}

DATABASE_ROUTERS = ['urbvan.routers.UrbvanRouter']

# The path depends of the library location in container
# GDAL_LIBRARY_PATH = '/home/sue/local/lib/libgdal.so'
