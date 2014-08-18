from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS, TEMPLATE_LOADERS, STATICFILES_FINDERS
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(BASE_DIR, '..')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ SECRET_KEY }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.pages',
    'crispy_forms',
    #'rosetta',
    
)
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'


MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{project_name}}.urls'

WSGI_APPLICATION = '{{project_name}}.wsgi.application'


# Database = NO DATABASE



LANGUAGE_CODE = 'en'
'''
# Enable for Internationalization and make the later settings to True

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)
LANGUAGES = (
    ('en', _('English')),
    ('el', _('Greek')),
)
TIME_ZONE = 'UTC'
'''
USE_I18N = False
USE_L10N = False
USE_TZ = False



TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'assets'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')



#You can enable the i18n context processor and use the provided view to change between languages (or use different links with en/el values before the rest of the link
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    #'django.core.context_processors.i18n',
)
#Lastly, point to the LOCALE folder in your project, that the translations should be stored.
#Run ./manage.py makemessage -l <language code> 
#for each language, to generate the language file. later, with compilemessages, you can install the translations you used.
'''

'''

#CRISPY FORMS SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'
