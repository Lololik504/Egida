STATIC_URL = "/admin/staticfiles/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'egida',
        'USER': 'egida',
        'PASSWORD': '101210',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
