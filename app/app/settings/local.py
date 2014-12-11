from base import *
from os import (
    environ,
    path)

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rtd2015',
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../../srv/assets'),
)

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../srv/static'))
STATIC_URL = 'http://local-static.researchthroughdesign.org/'

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../app/media'))
MEDIA_URL = 'http://local-media.researchthroughdesign.org/'
