import os
import dj_database_url
import django_heroku

# Configuração do banco de dados
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Verifica se estamos em ambiente local
if 'DATABASE_URL' not in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'mysql.connector.django',
            'NAME': 'escola',
            'USER': 'denizard',
            'PASSWORD': 'denizdeniz',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

# Configuração do Heroku
django_heroku.settings(locals())
