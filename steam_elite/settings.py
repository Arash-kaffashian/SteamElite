from pathlib import Path
import os
from datetime import timedelta
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------
# SECURITY & DEBUG
# ------------------------
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
IS_DEVEL = config("IS_DEVEL", default=True, cast=bool)

# Allowed hosts
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# ------------------------
# Applications
# ------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
    'drf_spectacular',

    'products',
    'user',
    'cart',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'steam_elite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'steam_elite.wsgi.application'

# ------------------------
# Database (PostgreSQL)
# ------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT', cast=int),
    }
}

# ------------------------
# Password validation
# ------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ------------------------
# Internationalization
# ------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------
# Static & Media
# ------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# ------------------------
# Cache: Redis
# ------------------------
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('REDIS_CACHE_URL'),
        'OPTIONS': {'CLIENT_CLASS': 'django_redis.client.DefaultClient'}
    }
}

CACHE_TTL = 180

# ------------------------
# Celery
# ------------------------
CELERY_BROKER_URL = config('REDIS_BROKER_URL')
CELERY_RESULT_BACKEND = config('REDIS_BACKEND_URL')
CELERY_TIMEZONE = "Asia/Tehran"
CELERY_ENABLE_UTC = True


# ------------------------
# Celery
# ------------------------
REDIS_HOST = config("REDIS_HOST", default="redis")
REDIS_PORT = config("REDIS_PORT", default="6379")

REDIS_CACHE_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
REDIS_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/1"
REDIS_DB_CACHE = config('REDIS_CACHE_URL')


# Celery Beat schedule example
CELERY_BEAT_SCHEDULE = {
    "refresh_steam_prices_every_2_min": {
        "task": "products.tasks.refresh_all_prices",
        "schedule": timedelta(minutes=2),
    },
}

# ------------------------
# Django REST Framework
# ------------------------
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'PAGE_SIZE': 10,
}

# Swagger Config
SPECTACULAR_SETTINGS = {
    'TITLE': 'My API',
    'DESCRIPTION': 'API documentation',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# ------------------------
# Default primary key field type
# ------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
