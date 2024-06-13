import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv()

environment = os.getenv('DJANGO_ENVIRONMENT', 'development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'src.config.settings.{environment}')

application = get_wsgi_application()
