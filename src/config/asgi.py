import os

from django.core.asgi import get_asgi_application
from dotenv import load_dotenv

load_dotenv()

environment = os.getenv('DJANGO_ENVIRONMENT', 'development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'src.config.settings.{environment}')

application = get_asgi_application()
