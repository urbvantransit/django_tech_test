# coding: utf8
from .base import *

# en la practica este archivo no se deberia agregar a git
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = \
    ('rest_framework.authentication.SessionAuthentication',) + REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']
