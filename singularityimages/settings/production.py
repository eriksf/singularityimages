import dj_database_url
from os import environ
from .base import *


DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = environ['STATIC_ROOT']
