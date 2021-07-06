from .base import *


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Reparapp',
        'USER':'root',
        'PASSWORD':'1234',
        'HOST':'localhost',
        'PORT':'',
    }
}
