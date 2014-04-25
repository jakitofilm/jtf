from jtf.settings import *   # pylint: disable=W0614,W0401

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory'
    }
}

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
COVER_PACKAGE = '--cover-package=' + ','.join(JTF_APPS)

NOSE_ARGS = [
    '--with-coverage',
    COVER_PACKAGE,
]

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

# quick dirty hack
import socket
if socket.gethostname() == 'laptop':
    JTF_WORKER_API_HOST = '127.0.0.1:5000'
