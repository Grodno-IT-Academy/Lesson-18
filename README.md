# Подготовка
```shell
pip install --upgrade setuptools wheel
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

# test!!!
# install heroku cli
https://id.heroku.com/login
- Create heroku account
- install heroku cli
  
  https://devcenter.heroku.com/articles/heroku-cli
  
Для мака и линукса это комманда в консоль а для видоуса нужно использовать установщика
```shell
brew tap heroku/brew && brew install heroku
```
Heroku очень хорошо сделаная платформа так-что надо внмиательно читать консоль-информацию и исправлять системные ошибки!
```shell
heroku login
```
заканчиваем логин в браузере
```shell
heroku git:remote -a classifier-grodno-it-academy
```
это подключит гит на heroku к нашей папке.  Можно проверить с:
```shell
git remote -v
```
по скольку github далеко не единственное место пользующееся git системой.

мы так-же можем создать новый проект из командной линии с помощю:
```shell
heroku create cutom_project_name
```
нам понадобиться ещё два pip модуля в нашем проекте
```shell
pipenv install gunicorn whitenoise
pipenv lock --pre
pipenv sync
```
heroku нужен requirements.txt файл
```shell
pipenv lock -r > requirements.txt
```
если кто не пользуется pipenv можно сделать
```shell
pip freeze > requirements.txt
```
heroku так-же нужно знать какой версией питона наш проект пользуется.  Для этого создаём `runtime.txt` файл и прописываем:
```
python-3.9.2
```
и ещё один файл по имени `Procfile`
```shell
atom Procfile
```
с внутреннастями
```text
web: gunicorn classificator.wsgi --log-file -
```
последнее приготовление к отправке не сервер это добавить наш domain в `settings.py`
```python
DEBUG = False
ALLOWED_HOSTS = [
  '127.0.0.1:8000',
  'classifier-grodno-it-academy.herokuapp.com',
]
```
в heroku нужно уточнить язык в settings табе buildpack

- put website to github repository
connect to github through heroku