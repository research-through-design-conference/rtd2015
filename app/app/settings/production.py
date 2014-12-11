from base import *

DEBUG = True

TEMPLATE_DEBUG = True

AWS_ACCESS_KEY_ID = "AKIAIWQKZQAOHXUXCAXQ"
AWS_SECRET_ACCESS_KEY = "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"

AWS_STORAGE_BUCKET_NAME = 'rtd2015'

STATICFILES_STORAGE = 'app.settings.s3utils.StaticRootS3BotoStorage'
DEFAULT_FILE_STORAGE = 'app.settings.s3utils.MediaRootS3BotoStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../../srv/assets'),
)

STATIC_ROOT = 'http://rtd2015.s3.amazonaws.com/static/'
STATIC_URL = 'http://rtd2015.s3.amazonaws.com/static/'

MEDIA_ROOT = 'http://rtd2015.s3.amazonaws.com/media/'
MEDIA_URL = 'http://rtd2015.s3.amazonaws.com/media/'
