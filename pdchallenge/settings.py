import os
from datetime import timedelta
import sys
import django_heroku

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(PROJECT_ROOT, 'templates')

LOG_DIR = os.path.join(BASE_DIR, 'log')
DOC_DIR = os.path.join(BASE_DIR, 'doc')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'local')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&64r8!8(i9aonz9)*mp2_zx^m$xl&la#p#h)3r5l7-a1#pf_wg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
THUMBNAIL_DEBUG = DEBUG
INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',

    # Third-Party Apps
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'bootstrap4',
    'django_markup',
    'markdownify',

    # Project Apps
    'place',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'pdchallenge.urls'

# CONFIG MARKDOWN
MARKDOWNIFY_STRIP = False
MARKDOWNIFY_MARKDOWN_EXTENSIONS = ['markdown.extensions.fenced_code', 'markdown.extensions.extra', ]

MARKDOWNIFY_WHITELIST_TAGS = [
    'a',
    'abbr',
    'b',
    'i',
    'li',
    'ol',
    'p',
    'strong',
    'ul',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'h7',
    'ul',
    'li',
    'div',
    'img',
    'pre',
    'code',
    'table',
    'thead',
    'tr',
    'th',
    'tbody',
    'td',
    'br',
]

MARKDOWNIFY_WHITELIST_ATTRS = [
    'src',
    'alt',
    'align',
    'href',
    'height',
    'target',
    'id',
    'class',
]

MARKDOWNIFY_WHITELIST_STYLES = [
    'color',
    'font-weight',
]
MARKDOWNIFY_WHITELIST_PROTOCOLS = [
    'http',
    'https',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
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

WSGI_APPLICATION = 'pdchallenge.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if ENVIRONMENT == 'local':

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'pdtest',
            'USER': 'pdtest',
            'PASSWORD': 'pdtest1234',
            'HOST': 'localhost',
            'PORT': '5432',
        },
    }


else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }

    }
    # FORÇAR HTTPS
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
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

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# ------------------------

if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# CONFIGURAÇÃO DE LOGS
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'file_info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR + '/info.log',
            'formatter': 'verbose',
            'encoding': 'UTF-8',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR + '/error.log',
            'formatter': 'verbose',
            'encoding': 'UTF-8',
        },
        'file_warning': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': LOG_DIR + '/warning.log',
            'formatter': 'verbose',
            'encoding': 'UTF-8',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'apps': {
            'handlers': ['mail_admins', 'console', 'file_info', 'file_error', 'file_warning'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

# CONFIGURAÇÃO DE AUTENTICAÇÃO
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),  # TODO:
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# CONFIGURAÇÃO API
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': None,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

SITE_HEADER = 'PlanD Backend Test'
SITE_TITLE = 'PlanD Backend Test'
INDEX_TITLE = 'DashBoard'

# CONFIG PARA HEROKU

# Collect static
STATIC_ROOT = os.path.join(BASE_DIR, 'staticbuild')

# Url in browser
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/readme'

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        },
        'Bearer': {
            'type': 'apiKey',
            'name': 'Auth-Token',
            'in': 'header'
        }
    }
}

try:
    from .settings_local import *
except ImportError:
    pass

django_heroku.settings(locals())
