#!/usr/bin/python
# -*- encoding:utf-8 -*-

"""
Django settings for app project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '12cs7)1+3t!+ofce8rc1f3r!6^et^l!gn40eik-lppe3uk8f-0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'persona',
    'Employee',
    'social_auth'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = [BASE_DIR,'plantillas']

AUTH_USER_MODEL = 'auth.User'


FACEBOOK_APP_ID='323815751157865'
FACEBOOK_API_SECRET='8fdfa769731bbed3f55c07be422a9aa5'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.yahoo.YahooBackend',
    'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    'social_auth.backends.contrib.disqus.DisqusBackend',
    'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    'social_auth.backends.contrib.orkut.OrkutBackend',
    'social_auth.backends.contrib.foursquare.FoursquareBackend',
    'social_auth.backends.contrib.github.GithubBackend',
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'social_auth.backends.contrib.live.LiveBackend',
    'social_auth.backends.contrib.skyrock.SkyrockBackend',
    'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    'social_auth.backends.contrib.readability.ReadabilityBackend',
    'social_auth.backends.contrib.fedora.FedoraBackend',
    'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

FACEBOOK_EXTENDED_PERMISSIONS = ['email']

FACEBOOK_PROFILE_EXTRA_PARAMS = {'localhost': 'mx_MX'}

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL    = '/login-error/'

TEMPLATE_CONTEXT_PROCESSORS = (
    
    'django.contrib.auth.context_processors.auth',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)




"""
#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth'
#    'social.apps.django_app.context_processors.backends',
#    'social.apps.django_app.context_processors.login_redirect',
#    ) 


TEMPLATE_CONTEXT_PROCESSORS = (
     "django.contrib.auth.context_processors.auth",
     "django.core.context_processors.debug",
     "django.core.context_processors.i18n",
     "django.core.context_processors.media",
     "django.core.context_processors.static",
     "django.contrib.messages.context_processors.messages",
     "allauth",
     "allauth.context_processors.allauth",
     "allauth.account.context_processors.account",
     )

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.google.GoogleOAuth2',
    ) 

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'tu-id-de-cliente'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'tu-código-secreto' 

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/tu-url/'

WHITELISTED_DOMAINS = ['axiacore.com', 'gmail.com']

SOCIAL_AUTH_PIPELINE = (
    # recibe vía backend y uid las instancias de social_user y user
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    # Recibe según user.email la instancia del usuario y lo reemplaza con uno que recibió anteriormente
    'social.pipeline.social_auth.social_user',
    # Trata de crear un username válido según los datos que recibe
    'social.pipeline.user.get_username',
    # Crea un usuario nuevo si uno todavía no existe
    'social.pipeline.user.create_user',
    # Trata de conectar las cuentas
    'social.pipeline.social_auth.associate_user',
    # Recibe y actualiza social_user.extra_data
    'social.pipeline.social_auth.load_extra_data',
    # Actualiza los campos de la instancia user con la información que obtiene vía backend
    'social.pipeline.user.user_details',
) 

"""

