import os

from django.utils.translation import ugettext_lazy as _

import jtf as project_module


BASE_DIR = os.path.dirname(os.path.realpath(project_module.__file__))
VAR_ROOT = os.path.join(BASE_DIR, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5)9mc854#8+r%1=1n#3n$^*txw$zl4(v*%&p35l01a8*j_a2)e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

APPEND_SLASH = True

# Application definition


JTF_APPS = [
    'jtf.apps.core',
]

EXTENDED_EXTERNAL_APPS = [
    'jtf.ex.parler',
]

EXTERNAL_APPS = [
    'suit',
    'compressor',
    'django_extensions',
    'parler',
    'polymorphic',
    'reversion',
    'sorl.thumbnail',
    'south',
]

DJANGO_APS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]

SITE_ID = 1

INSTALLED_APPS = JTF_APPS + EXTENDED_EXTERNAL_APPS + EXTERNAL_APPS + DJANGO_APS

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

ROOT_URLCONF = 'jtf.urls'

WSGI_APPLICATION = 'jtf.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pl'
LANGUAGES = (
    ('pl', _('Polish')),
    ('en', _('English')),
    ('de', _('German')),
    ('it', _('Italian')),
    ('fr', _('French')),
    ('es', _('Spanish')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder'
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'media')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

PARLER_DEFAULT_LANGUAGE = LANGUAGE_CODE

PARLER_LANGUAGES = {
    1: (
        {'code': 'pl'},
        {'code': 'en'},
        {'code': 'de'},
        {'code': 'fr'},
        {'code': 'it'},
        {'code': 'es'},
    ),
    'default': {
        'fallback': 'pl',
    }
}

JTF_WORKER_API_HOST = 'jtf_worker.eu01.aws.af.cm'
