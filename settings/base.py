# -*- coding: utf-8 -*-

import os
from collections import OrderedDict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE_SIZE = 2 
SECRET_KEY = 'asdfasdfasd'
DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.blog.context_processors.theme',
            ],
        },
    },
]

ALLOWED_HOSTS = ['vatualvenue.xyz',
                 'vatualvenue.xyz.',
                 'vatualvenue.xin',
                 'vatualvenue.online',
		 '127.0.0.1',
		 '*',
                 'vatualvenue.xin.',]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'apps.blog',
    'pagedown',
    'compressor',
]
SITE_ID = 1
MIDDLEWARE_CLASSES = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Myblog',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'zh-hans'

USE_I18N = True
USE_L10N = True
USE_TZ = False

GOOGLE_ANALYTICS_ID = 'you google analytics id'
DISQUS_NAME = "YOU DISQUE SHORT NAME"

SIMPLEMDE_OPTIONS = {
    'placeholder': 'haha',
    'status': False,
    'autosave': {
        'enabled': True
    }
}

# ---------------------------------------------------------------
# 主题配置
# ---------------------------------------------------------------
SITE_TITLE = "Virtualvenue's Blog"
SITE_SUBTITLE = u"My World"
KEYWORDS = "virtualvenue, Python"

# ---------------------------------------------------------------
# Menu Settings
# ---------------------------------------------------------------
MENU = OrderedDict(sorted({"home": {"label": u"首页", "path": "/", "icon": "home", "position": 1},
                           "categories": {"label": u"分类", "path": "/categories", "icon": "th", "position": 3},
                           "archives": {"label": u"归档", "path": "/archives", "icon": "archive", "position": 2},
                           "tags": {"label": u"标签", "path": "/tags", "icon": "tags", "position": 4},
                           "about": {"label": u"关于", "path": "/about", "icon": "user", "position": 5}, }.items(),
                          key=lambda t: t[1]['position']))

SCHEME = "Pisces"

SOCIAL = OrderedDict(
    sorted({"GitHub": {"label": u"GitHub", "link": "https://github.com/470434839", "social_icons": "github",
                       "position": 1},
          
                       
            "Zhihu": {"label": u"知乎", "link": "https://www.zhihu.com/people/wang-shuo-1-15/activities", "social_icons": "",
                      "position": 5},

            }.items(), key=lambda t: t[1]['position']))

SIDEBAR = {"position": "left",
           "display": "post"
           }

DUOSHUO_SHORTNAME = "virtualvenue"
GOOGLE_SITE_VERIFICATION = "your google site verification"
GOOGLE_ANALYTICS = "you google analytics id"
USE_MOTION = True
FANCYBOX = True
RSS = '/rss'
VERSION = '5.0.1'
ALIPAY = ""
WECHATPAY = ""

