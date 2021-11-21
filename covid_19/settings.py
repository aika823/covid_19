import os
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))
SECRET_DIR = os.path.join(PROJECT_ROOT, "secret")
SECRETS = json.load(open(os.path.join(SECRET_DIR, "secret.json"), "rb"))
SECRET_KEY = SECRETS["SECRET_KEY"]

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "django-env.eba-rwsncwpq.ap-northeast-2.elasticbeanstalk.com",
]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'covid',
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

ROOT_URLCONF = 'covid_19.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'covid_19.wsgi.application'


# Database
SECRET_DIR = os.path.join(PROJECT_ROOT, "secret")

DB_SECRETS = json.load(open(os.path.join(SECRET_DIR, "database.json"), "rb"))
DATABASES = {
    "default": {
        "ENGINE": DB_SECRETS["ENGINE"],
        "NAME": DB_SECRETS["NAME"],
        "USER": DB_SECRETS["USER"],
        "PASSWORD": DB_SECRETS["PASSWORD"],
        "HOST": DB_SECRETS["HOST"],
        "PORT": DB_SECRETS["PORT"],
        "OPTIONS": DB_SECRETS["OPTIONS"],
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "static/css"),
    os.path.join(BASE_DIR, "static/img"),
    os.path.join(BASE_DIR, "static/js"),
    "static/css",
    "static/js",
    "static/img",
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


