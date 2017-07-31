"""
Django settings for Social project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.core.urlresolvers import reverse_lazy


LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN = reverse_lazy('login')
LOGOUT = reverse_lazy('logout')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g#sx#-ny+wftn@#*9#42bir==lg62f_0%$t(%xfzr8a_c=c_km'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'account',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'images',
    'sorl.thumbnail',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Social.urls'

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

WSGI_APPLICATION = 'Social.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Send Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 994
EMAIL_HOST_USER = 'XXXX@gmail.com'
EMAIL_HOST_PASSWORD = 'E8FCzckQ'
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = 'XXX@gmail.com'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# add custom authentication
# 按排列顺序逐一认证
# 认证会存储在用户的session里
AUTHENTICATION_BACKENDS = (
    # 系统默认认证,不支持暴力破解保护
    'django.contrib.auth.backends.ModelBackend',
    # 扩展EMAIL认证
    'account.authentication.EmailAuthBackend',
    # github认证
    'social.backends.github.GithubOAuth2',
)

SOCIAL_AUTH_GITHUB_KEY = '242d25d2a05e410a92c5'
SOCIAL_AUTH_GITHUB_SECRET = '284341b639cfc7a78c82bfeed5d95f09cd20818c'
