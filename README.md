# Подготовка
```shell
pip install --upgrade pipenv
```
вышла новая версия  `pipenv`
# Работа с Postgres
Postgres это структура базы данных типа sql которой мы пользуемся с нашей sqlite3 базой в файле `db.splite3`.  Проблемы здесь две, одна мы не можем посмотреть на данные в этой базе и она распологаеться в файловом пространстве нашего проекта что не очень безопасно и не позволит нашему серверу децентрализироваться.  Поэтому мы сделаем миграцию в postgres и в дальнейшем наш проект подключим к виртуальному серверу расположеному в стокгольмском отделе амазона.
```shell
pipenv install psycopg2-binary
pipenv lock --pre
pipenv sync
```
Позволит питону работать с нашей базой данных
```python

# STEPS FOR DJANGO POSTGRESQL DATABASE + AWS RDS
# 1 - Download and install PostgreSQL & PG Admin
# 2 - Login to PG admin & Create Database
# 3 - Connect database to Django App & run migrations
# 4 - Create database on AWS
# 5 - Connect to live AWS Database with PG admin & Django


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database name',
        'USER':'database user',
        'PASSWORD':'database password',
        'HOST':'database endpoint',
        'PORT':'database port'
    }
}

```


#S3 BUCKETS CONFIG

'''

AWS_ACCESS_KEY_ID = '*****************'

AWS_SECRET_ACCESS_KEY = '*****************'

AWS_STORAGE_BUCKET_NAME = '*****************'



AWS_S3_FILE_OVERWRITE = False

AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

'''







'''

<?xml version="1.0" encoding="UTF-8"?>

<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">

<CORSRule>

    <AllowedOrigin>*</AllowedOrigin>

    <AllowedMethod>GET</AllowedMethod>

    <AllowedMethod>POST</AllowedMethod>

    <AllowedMethod>PUT</AllowedMethod>

    <AllowedHeader>*</AllowedHeader>

</CORSRule>

</CORSConfiguration>



'''
