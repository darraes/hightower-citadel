## Created based on 
https://realpython.com/django-setup/

## Run
python3 manage.py runserver

## Migrations can be refreshed using the following
python3 manage.py makemigrations citadel && python3 manage.py migrate

## Starting of for testing
python manage.py createsuperuser --username=admin --email=admin@admin.com

## Check typing
mypy -p citadel --strict --exclude "migration|apps"

## Test Login Payload
{
    "username": "admin",
    "password": "###"
}

## Authentication was done using
https://testdriven.io/blog/django-rest-authjs/

## TODO
 - Eval the usage of ```from django.http import JsonResponse```