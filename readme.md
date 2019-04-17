# Test Driven Development Tutorial

## simple project showcasing how to implement tdd - functional and unit testing; built using DRF (django-rest framework)

## install

- clone repo
- make virtual env with python 3.6
- install requirements:
```
pip install -r requirements.txt
```
- create .env file in project root
```
SECRET_KEY=***some-secret-key***
DEBUG=True
ALLOWED_HOSTS=*,
```
- create .env files in /ft and /ut folders
- run migrations:
```
python manage.py migrate
```
- add fixtures:
```
python manage.py loaddata
```
- run tests
