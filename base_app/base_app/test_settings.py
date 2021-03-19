from .settings import *

DATABASE = {
    "default":{
        "ENGINE": 'django.db.backend.sqlite3',
        "NAME": 'memory',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
