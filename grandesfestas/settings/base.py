import os
import sys
from os.path import join, abspath, dirname
from grandesfestas.apps.preferences.lazy_settings import LazyStringSetting, LazyBooleanSetting


# PATH vars
def here(*x):
    return join(abspath(dirname(__file__)), *x)


def root(*x):
    return join(abspath(PROJECT_ROOT), *x)

PROJECT_ROOT = here("..")
REPOSITORY_ROOT = dirname(root())

sys.path.insert(0, root('apps'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE THIS!!!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dynamic_preferences',
    'rest_framework',
    'paypal.standard.ipn',
    'import_export',
    'rosetta',
)

PROJECT_APPS = (
    'staticcontent',
    'preferences',
    'volunteers',
    'trainings',
    'subscriptions',
    'apiv1',
)

INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'dynamic_preferences.processors.global_preferences'
)


ROOT_URLCONF = 'grandesfestas.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'grandesfestas.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB', 'grandesfestas'),
        'USER': os.getenv('USER', 'fabio'),
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = False

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = root('assets', 'uploads')
MEDIA_URL = '/media/'

# Additional locations of static files

STATICFILES_DIRS = (
    root('assets'),
)

TEMPLATE_DIRS = (
    root('templates'),
)

PAYPAL_TEST = LazyBooleanSetting('payment__paypal_test')
PAYPAL_RECEIVER_EMAIL = LazyStringSetting('payment__paypal_receiver_email')

FORMAT_MODULE_PATH = [
    'grandesfestas.formats',
]

LOCALE_PATHS = (
    root('locale'),
)


ROSETTA_MESSAGES_PER_PAGE = 100
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
ROSETTA_GOOGLE_TRANSLATE = True

# .local.py overrides all the common settings.
try:
    from .local import *
except ImportError:
    pass


# importing test settings file if necessary
if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    from .testing import *
