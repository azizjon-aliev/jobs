from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

LOGGING['handlers']['console']['level'] = 'ERROR'
LOGGING['handlers']['file']['level'] = 'ERROR'
