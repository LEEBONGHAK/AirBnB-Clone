"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "yn0^c1hz(+b+3c&ju3go780wtcxt=+wsr2z+=)hs177-=s)5n&"

# 프로덕션인지 개발인지 감지할 수 있는 것
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "rooms.apps.RoomsConfig",
    "reviews.apps.ReviewsConfig",
    "reservations.apps.ReservationsConfig",
    "lists.apps.ListsConfig",
    "conversations.apps.ConversationsConfig",
]

THIRD_PARTY_APPS = [
    "django-countries",
    "django_seed",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"  # 이 url로 접속하면 static 폴더의 내용에 접근할 수 있음

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]  # 기본적으로 /static/에 가면 접근할 수 있는 파일을 보여주는 것

AUTH_USER_MODEL = "users.User"

# 장고에게 어디에 업로드한 파일들을 써야할 지 말해주는 곳 => 절대 파일 경로 지정해주어야 함
# (이미 BASE_DIR을 위한 절대 경로 패스를 가지고 있음 => join을 통해 원하는 절대경로 지정)
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")

# url을 컴퓨터 안의 폴더와 연결 시키기
# url이 디렉토리명과 같을 필요는 없음
# 디렉토리로부터 뭔가를 가져오고 싶다면 디렉토리의 하위 디렉토리로 갈 수 있게 설정 => config의 url.py에 추가!!!
# 앞에 '/'을 추가해 주면 상대 경로에서 절대 경로로 변경
MEDIA_URL = "/media/"

# Email Configuration - using mailgun
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = "587"
EMAIL_HOST_USER = os.environ.get("MAILGUN_USERNAME")
EMAIL_HOST_PASSWORD = os.environ.get("MAILGUN_PASSWORD")
EMAIL_FROM = "sexy-guy@sandbox2ba559537f904296851b8b1b0c8d7d24.mailgun.org"


# Auth
LOGIN_URL = "/users/login/"


# Lacale
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

# language
LANGUAGE_COOKIE_NAME = "django_language"