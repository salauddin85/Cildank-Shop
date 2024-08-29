

"""
Django settings for fashionfusion_shop project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

from pathlib import Path
import environ
env = environ.Env()
environ.Env.read_env()
import os
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import cloudinary



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-0j+z#n^nhip@udt7mtd++z@e2l*8r+5nt*2t*c^8mw@!ws%kwe'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True  # ডেভেলপমেন্টের জন্য
CORS_ALLOW_ALL_ORIGINS = True  # শুধুমাত্র ডেভেলপমেন্টে ব্যবহারের জন্য
ALLOWED_HOSTS = ["*"]
LOGIN_URL = "https://cildank-shop.onrender.com/login.html"  # প্রয়োজন অনুযায়ী
CSRF_TRUSTED_ORIGINS = ['https://cildank-shop.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'auth_app',
    'cloth_category',
    'cloth_product',
    'Purchase',
    'Transactions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'Cildank_Cloth_Shop.urls'

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

WSGI_APPLICATION = 'Cildank_Cloth_Shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': env("DB_NAME"),
#         'USER': env("DB_USER"),
#         'PASSWORD': env("DB_PASSWORD"),
#         'HOST': env("DB_HOST"),
#         'PORT': env("DB_PORT"),
#     }
# }

DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://cildank_shop_user:q0ylVYIQZVKhoABeUfJcQXGW2sZkiJz9@dpg-cr66mortq21c73ba9ifg-a.oregon-postgres.render.com/cildank_shop',
        
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SECRET_KEY = env("SECRET_KEY")
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
# settings.py
APPEND_SLASH = False


# REST_FRAMEWORK = {
    
#     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
#      'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
        
#     ],
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    # Other settings...
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os

# Set the CLOUDINARY_URL using the provided value
# CLOUDINARY_URL = os.env('CLOUDINARY_URL', 'cloudinary://464615231665312:CGMQbVMG6UJOS7zSsY9AlOlX6S0@dnzqmx8nw?secure_distribution=mydomain.com&upload_prefix=myprefix.com')

import cloudinary.uploader
import cloudinary.api
CLOUDINARY_URL='cloudinary://464615231665312:CGMQbVMG6UJOS7zSsY9AlOlX6S0@dnzqmx8nw'
cloudinary.config(
    cloud_name="dnzqmx8nw",
    api_key="464615231665312",
    api_secret="CGMQbVMG6UJOS7zSsY9AlOlX6S0"
)

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': 'dnzqmx8nw',
#     'API_KEY': '464615231665312',
#     'API_SECRET': 'CGMQbVMG6UJOS7zSsY9AlOlX6S0',
# }

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

