import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(__file__)

SECRET_KEY = '@6(ze%9_(^2a^hi2^ojet#jyr-w7s0s%uthtu)x&4m55v+-o-r'

# SECURITY WARNING: don't run with debug turned on in production!
if socket.gethostname() == '85964.local':
    DEBUG = False
    PUBLIC_DIR = '/var/www/opentalks/public/'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': 'projector',
    #         'USER': 'postgres',
    #         'PASSWORD': 'password',
    #         'HOST': 'localhost',
    #         'PORT': '5432',
    #     },
    # }
    ALLOWED_HOSTS = ['*']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    SITE_ID = 1

else:
    DEBUG = True
    PUBLIC_DIR = os.path.join(PROJECT_DIR, 'public')
    TEST_MODE = True
    SITE_ID = 1
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    ALLOWED_HOSTS = ['*']
    # print('Debug = True')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


STATIC_ROOT = os.path.join(PUBLIC_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(PUBLIC_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'core',
    'event',
    'froala_editor',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
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

ROOT_URLCONF = 'opentalks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # ...
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    # ...
)

WSGI_APPLICATION = 'opentalks.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

AUTH_USER_MODEL = 'core.User'
ACCOUNT_FORMS = {'signup': 'core.forms.SignupForm'}

ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_UNIQUE_USERNAME = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"

# AUTH_USER_MODEL = 'auth'
LOGIN_REDIRECT_URL = '/'


# FROALA_INCLUDE_JQUERY = False

FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier', 'code_view', 'colors', 'draggable', 'emoticons',
                         'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image',
                         'inline_style',
                         'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert',
                         'quote', 'save', 'table',
                         'url', 'video')

FROALA_UPLOAD_IMAGES_PATH = os.path.join(MEDIA_ROOT, 'froala/images')
FROALA_UPLOAD_IMAGES_URL = '/media/froala/images/'



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d', '%m-%d-%Y')

