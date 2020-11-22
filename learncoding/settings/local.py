from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n4%=@kb-sj%d)8fpy1ltmm6o69$ujo46yoe8w1ffo9+i5&do0d'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
