from .base import *

DEBUG = True

INSTALLED_APPS = [
    *INSTALLED_APPS,
    'drf_spectacular',
]

REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Jobs Project API',
    'DESCRIPTION': 'Jobs project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    "SPECTACULAR_DEFAULTS": {
        "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
    },
    "SCHEMA_PATH_PREFIX": r"/api/v[0-9]+/[a-zA-Z]+/",
    "COMPONENT_SPLIT_REQUEST": True,
}
