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
    'db_read': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_read.sqlite3'),
    }
}

DATABASE_ROUTERS = ['urbvan.routers.UrbvanRouter']
