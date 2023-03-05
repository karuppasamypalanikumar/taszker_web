from pathlib import Path
import environ

# ----------------------------------------------------------------
# Initialise environment variables
# ----------------------------------------------------------------

env = environ.Env()
environ.Env.read_env()

# ----------------------------------------------------------------
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# ----------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------------------------------------
# SECURITY WARNING: keep the secret key used in production secret!
# ----------------------------------------------------------------

SECRET_KEY = 'django-insecure-mt=+u3sdzce%9zfexip69p=uuaw8gz3_yw_y0gpwn1#=xyy7k@'

ALLOWED_HOSTS = ['*']

# ----------------------------------------------------
# Application definition
# ----------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'account',
    'task',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'base.wsgi.application'

# ------------------------------------------------------
# Hosting Setting
# ------------------------------------------------------
ALLOWED_HOSTS = ['*']

# -------------------------------------------------------
# Rest Framework Settings
# -------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':10
}

# --------------------------------------------------------------
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
# --------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# --------------------------------------------------------------
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
# --------------------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# --------------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# --------------------------------------------------------------

STATIC_URL = 'static/'


# --------------------------------------------------------------
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
# --------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'