import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = True
DJANGO_ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT')

ALLOWED_HOSTS = []

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {
			# 'format': '{asctime} - {levelname} - {module} - {filename} - {name} - {args} - {message} - {msg}',
			'format': '{asctime} - {levelname} - {name} - {funcName} - {args} - {msg}',
			'style': '{',
		},
	},
	'handlers': {
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'verbose',
		},

		'file': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',
			'filename': 'django.log',
			'formatter': 'verbose',
		},
	},
	'loggers': {
		'': {
			'handlers': ['console', 'file'],
			'level': 'INFO',
		},
	},
}

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# libraries
	'rest_framework',
	# apps
	'src.apps.common',
	'src.apps.vacancy',
]

REST_FRAMEWORK = {
	'DEFAULT_RENDERER_CLASSES': [
		'rest_framework.renderers.JSONRenderer',
	],
	'DEFAULT_PARSER_CLASSES': [
		'rest_framework.parsers.JSONParser',
	],
	'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
	'ALLOWED_VERSIONS': ['v1', 'v2'],
	'DEFAULT_VERSION': 'v1',
}

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.config.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'src.config.wsgi.application'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
