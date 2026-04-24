from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Security: Use environment variable for SECRET_KEY
# Generate a new key with: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-j&hjb3ypz=33k0kr0g1t(qi^4pyz0dy**jm&y*qalq7q)q&o@g')

# Security: DEBUG should be False in production
# Set DJANGO_DEBUG=False in environment variables for production
DEBUG = os.environ.get('DJANGO_DEBUG', 'True').lower() in ('true', '1', 'yes')

# Security: ALLOWED_HOSTS should only contain production domains
# Set DJANGO_ALLOWED_HOSTS in environment (comma-separated) for production
allowed_hosts_env = os.environ.get('DJANGO_ALLOWED_HOSTS', '')
if allowed_hosts_env:
    ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_env.split(',')]
else:
    # Development defaults
    ALLOWED_HOSTS = ['panel.sarafipardis.co.uk', 'www.panel.sarafipardis.co.uk', "localhost", "127.0.0.1", "admin.sarafipardis.co.uk", "www.admin.sarafipardis.co.uk"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps
    'category',
    'dashboard',
    'accounts',
    'change_price',
    'special_price',
    'telegram_app',
    'setting',
    'finalize',
    'price_publisher',
    'template_editor',
    'analysis',
    'landing',
    'instagram_hub',
    # third-party apps
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'accounts.auth.JWTAuthenticationWithTokenVersion',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'EXCEPTION_HANDLER': 'core.exceptions.custom_exception_handler',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '1000/hour',
        'finalize': '60/hour',
        'settings': '200/hour',
    },
}

# Finalize: when True, do not persist finalization if Telegram publish fails (rollback semantics).
# When False, persist with message_sent=False on Telegram failure.
FINALIZE_STRICT_TELEGRAM = os.environ.get('FINALIZE_STRICT_TELEGRAM', 'False').lower() in ('true', '1', 'yes')

from datetime import timedelta as _td  # noqa: E402

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': _td(hours=12),
    'REFRESH_TOKEN_LIFETIME': _td(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
CORS_ALLOW_CREDENTIALS = True

# Required when the SPA runs on another origin/port (e.g. Vite :5173) and proxies API
# to Django: the browser sends Origin: http://localhost:5173 while Host may be backend:8000.
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
_csrf_extra = os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS', '').strip()
if _csrf_extra:
    CSRF_TRUSTED_ORIGINS = list(
        dict.fromkeys(CSRF_TRUSTED_ORIGINS + [o.strip() for o in _csrf_extra.split(',') if o.strip()])
    )

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Enforce login for all views (allows exceptions in middleware)
    'accounts.middleware.LoginRequiredMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Custom 404 middleware to show custom 404 page even when DEBUG=True
    'SmartExchangePanel.middleware.Custom404Middleware',
]

ROOT_URLCONF = 'SmartExchangePanel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Custom templates path
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'setting.context_processors.site_settings_processor',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SmartExchangePanel.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ.get('SQLITE_PATH', str(BASE_DIR / 'db.sqlite3')),
    }
}

# Caching - Removed: No caching is used in this application

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tehran'  # Change to Iran's time zone
USE_I18N = True
USE_TZ = True

# -----------------------------
# Static & Media configuration
# -----------------------------

# URL address for static files
STATIC_URL = '/static/'
# Public base URL for media (required for Instagram: Meta fetches images from this URL)
INSTAGRAM_BASE_URL = os.environ.get('INSTAGRAM_BASE_URL', '').strip()
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Location of static files in development
]
STATIC_ROOT = BASE_DIR / 'public' / 'staticfiles'  # Collection location for files in production

# URL address for uploaded files (images, etc.)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'public' / 'media'

# -----------------------------
# Template & Rendering extras
# -----------------------------
TEMPLATE_EDITOR_DEFAULT_FONT = str(BASE_DIR / 'static' / 'fonts' / 'Kalameh.ttf')
PRICE_RENDERER_FONT_ROOT = BASE_DIR / 'static' / 'fonts'
LEGACY_CATEGORY_BACKGROUNDS = {
    "pound": "price_theme/1.png",
    "gbp": "price_theme/1.png",
    "پوند": "price_theme/1.png",
}

# -----------------------------
# Other settings
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Custom user model and auth settings
AUTH_USER_MODEL = 'accounts.CustomUser'
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# -----------------------------
# External API (sarafipardis.co.uk rates)
# -----------------------------
EXTERNAL_API_URL = os.environ.get(
    'EXTERNAL_API_URL',
    'https://sarafipardis.co.uk/wp-json/pardis/v1/rates'
)
EXTERNAL_API_KEY = os.environ.get(
    'EXTERNAL_API_KEY',
    'PX9k7mN2qR8vL4jH6wE3tY1uI5oP0aS9dF7gK2mN8xZ4cV6bQ1wE3rT5yU8iO0pL'
)

# Security settings
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    # Additional security headers
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'
else:
    # In development, disable secure cookies for easier testing
    SECURE_SSL_REDIRECT = False
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
    # Still enable some security headers in development
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'

# RBAC debug: log permission checks (user/role) when DEBUG is True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {'format': '%(levelname)s %(name)s: %(message)s'},
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'accounts.permissions': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
