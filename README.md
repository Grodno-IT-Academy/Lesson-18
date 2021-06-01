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
        'NAME': 'DEMO_TEST',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```
после установки новой базы и подключения проверьте пользуясь:
```shell
python manage.py migrate
```
## Создай aws счёт
## Открой новую базу данных на AWS
Эти шаги мне не удались дома. Я думаю интернет не позволяет.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_1',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'database-2.cxh4hqdaiqm7.eu-north-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
```
# AWS S3 Bucket Setup
зайти в aws и найти s3 создать бакет
в permissions изменить cors на:
```json
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET",
            "POST",
            "PUT"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```
зайди в IAM (identity access managment)
- create user
- attache existing policies
    - AmazonS3FullAccess
    
Это позволит нам загружать файлы

```python
#S3 BUCKETS CONFIG


AWS_ACCESS_KEY_ID = 'AKIA5BO6KSV5OR4PDKX2'

AWS_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'mikhailclassifier'

AWS_S3_REGION_NAME = 'eu-north-1'
```
дальше мы воспользуемся модулем `django-storages`
```shell
pipenv install django-storages
pipenv lock --pre
pipenv sync
```
`storages` зависим от `boto3` в использовании амазон-серверов так-что придётся установить и их!
```shell
pipenv install boto3
pipenv lock --pre
pipenv sync
```
https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
```python
AWS_S3_FILE_OVERWRITE = False

AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```
- upload files with folders to s3






