

STATIC_URL = "/back-end/admin/staticfiles/"

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
