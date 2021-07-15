import os
from pathlib import Path

import datetime

from . import log_settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TIME_ZONE = 'Asia/Novosibirsk'

# SECRET_KEY = 's_guh_fk#z)4r!7fb)^oug*@=d9_zx36cb0+lbccjd9mo&e1ra'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 's_guh_fk#z)4r!7fb)^oug*@=d9_zx36cb0+lbccjd9mo&e1ra')

# PROD = bool(os.environ.get('DJANGO_PROD', False))
PROD = bool(os.environ.get('DJANGO_PROD', True))

LOG_DIR = os.path.join(BASE_DIR, "log/")

log_settings.setup_settings()

DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_HEADERS = ['*']

CORS_ALLOW_CREDENTIALS = True

# AUTH_USER_MODEL = 'accounts.MyUser'

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django_summernote',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'drf_yasg',

    'corsheaders',
    'main',
    'accounts',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.AllowAny',
    ),
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.PageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'

}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "Egida.middleware.MyAuthenticationMiddleware"
]

ROOT_URLCONF = 'Egida.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'Egida.wsgi.application'

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

SITE = 1

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/back-end/admin/staticfiles/"

# STATICFILES_DIRS = [
#     BASE_DIR / "assets",
# ]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

DOCUMENT_ROOT = os.path.join(BASE_DIR, "media/docs")

DOCUMENT_URL = 'docs'

ORDERS_ROOT = os.path.join(BASE_DIR, "media/orders")

ORDERS_URL = 'orders'

ROSPOTREB_ROOT = os.path.join(BASE_DIR, "media/orders/rospotrebnadzor")
GOSPOZH_ROOT = os.path.join(BASE_DIR, "media/orders/gospozhnadzor")
ROSTECH_ROOT = os.path.join(BASE_DIR, "media/orders/rostechnadzor")
SUDEB_ROOT = os.path.join(BASE_DIR, "media/orders/sudebresh")
OTHER_ORDERS_ROOT = os.path.join(BASE_DIR, "media/orders/otherorders")

ROSPOTREB_URL = 'rospotreb'
GOSPOZH_URL = 'gospozh'
ROSTECH_URL = 'rostechnadzor'
SUDEB_URL = 'sudebresh'
OTHER_ORDERS_URL = 'otherorders'

BUILDING_MEDIA_ROOT = os.path.join(BASE_DIR, "media/building_media")
BUILDING_MEDIA_URL = 'building_media'

ENGINEERING_COMMUNICATION_ROOT = os.path.join(BASE_DIR, "media/engineering_communication")
ENGINEERING_COMMUNICATION_URL = 'engineering_communication'

INDOOR_AREAS_ROOT = os.path.join(BASE_DIR, "media/engineering_communication")
INDOOR_AREAS_URL = 'indoor_areas'

UPDADTER_PRIKAZ_ROOT = os.path.join(BASE_DIR, 'media/updater_prikaz')
UPDADTER_PRIKAZ_URL = 'updater_prikaz'

MANDATE_ROOT = os.path.join(BASE_DIR, 'media/mandate')
MANDATE_URL = 'mandate'

if not os.path.exists(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)

if not os.path.exists(DOCUMENT_ROOT):
    os.mkdir(DOCUMENT_ROOT)

if not os.path.exists(ORDERS_ROOT):
    os.mkdir(ORDERS_ROOT)

for i in [ROSPOTREB_ROOT, GOSPOZH_ROOT, ROSTECH_ROOT, SUDEB_ROOT, OTHER_ORDERS_ROOT]:
    if not os.path.exists(i):
        os.mkdir(i)

if not os.path.exists(BUILDING_MEDIA_ROOT):
    os.mkdir(BUILDING_MEDIA_ROOT)

if not os.path.exists(ENGINEERING_COMMUNICATION_ROOT):
    os.mkdir(ENGINEERING_COMMUNICATION_ROOT)

if not os.path.exists(INDOOR_AREAS_ROOT):
    os.mkdir(INDOOR_AREAS_ROOT)

if not os.path.exists(UPDADTER_PRIKAZ_ROOT):
    os.mkdir(UPDADTER_PRIKAZ_ROOT)

if not os.path.exists(MANDATE_ROOT):
    os.mkdir(MANDATE_ROOT)

if PROD:
    from .prod_settings import *
else:
    try:
        from .local_settings import *
    except ImportError:
        from .prod_settings import *
