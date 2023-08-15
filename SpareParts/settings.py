"""
Django settings for SpareParts project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#pointing to the directory /root for the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#key is required for the project to run
SECRET_KEY = '%=0&*4hyq=3)(r%ck@5i-!l4_czs4i_)k@g$-r)65lqfd^oi9l'

# SECURITY WARNING: don't run with debug turned on in production!
#it lets django to allow me debug by displaying messages
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'StockApp',
    'crispy_forms',
    'crispy_bootstrap4',
    'bootstrap5',
    'django_filters',
]

#handle security  like csrf-token,login ,flash messages
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#defines the path for the urls of the project
ROOT_URLCONF = 'SpareParts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #states the location of the templates in the project BASE_DIRECTORY.
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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
#for deployment over the cloud
WSGI_APPLICATION = 'SpareParts.wsgi.application'


# Database configuration
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
#django find static files here,defining path for our static folder
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIR = [
    os.path.join(BASE_DIR,'StockApp/static')

    
]

#creating the base pack for crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

#successfull user will be redirected here after login
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'logout'