from .base import *

from .base import env

SECRET_KEY = env.str("DJANGO_SECRET_KEY","django-insecure-pmtb92asarfhx+sy^au0*(0np3)&-o3*jmo^h*m!tbm+b8y1ty")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS=["http://localhost:8080"]