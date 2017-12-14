from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = bool(int(os.getenv('DEBUG', True)))