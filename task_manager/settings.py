import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['webserver', 'localhost', '127.0.0.1', '.onrender.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'task_manager',
    'django_bootstrap5',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'task_manager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'task_manager.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = '/login/'

# =================== ROLLBAR CONFIGURATION ===================
def get_rollbar_config():
    config = {
        'access_token': os.getenv('ROLLBAR_ACCESS_TOKEN'),
        'environment': 'production' if not DEBUG else 'development',
        'code_version': '1.0.0',
        'root': BASE_DIR,
    'handler': 'blocking',
    }
    if not DEBUG:
        config['exception_level_filters'] = [
            ('django.http.Http404', 'warning'),
        ]
        config['scrub_fields'] = [
            'password', 'secret', 'token', 'api_key',
            'access_token', 'authorization', 'cookie',
            'csrf_token', 'sessionid',
        ]
    return config

ROLLBAR = get_rollbar_config()
# =============================================================

# Инициализация Rollbar
import rollbar
import rollbar.contrib.django

rollbar.init(
    os.getenv('ROLLBAR_ACCESS_TOKEN'),
    'development' if DEBUG else 'production',
    handler='blocking'
)

MIDDLEWARE.append('rollbar.contrib.django.middleware.RollbarNotifierMiddleware')
