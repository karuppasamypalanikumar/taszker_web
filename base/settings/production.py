from pathlib import Path
import environ
from .base import *

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),   # Or an IP Address that your DB is hosted on
        'PORT': '5432',
    }
}
