import os

STATIC_URL = "/back-end/admin/staticfiles/"

if os.environ.get('DB_LOCATION') == 'EGIDA':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'egida_schools',
            'USER': 'egida_admin',
            'PASSWORD': '101210',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dcgcp4ge8ohjj5',
            'USER': 'hwesktiefkymwv',
            'PASSWORD': '4a42a05abb76362608816ef8219ed3e711a9937d2f5afd1569237fc50904b0ef',
            'HOST': 'ec2-54-228-209-117.eu-west-1.compute.amazonaws.com',
            'PORT': '5432'
        }
    }
    