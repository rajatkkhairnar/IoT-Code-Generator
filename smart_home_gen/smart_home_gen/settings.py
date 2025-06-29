import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'change-me'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'generator',
]
MIDDLEWARE = ['django.middleware.common.CommonMiddleware']
ROOT_URLCONF = 'smart_home_gen.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': ['django.template.context_processors.request'],
    },
}]

WSGI_APPLICATION = 'smart_home_gen.wsgi.application'
DATABASES = {}
STATIC_URL = '/static/'