## Created based on 
https://realpython.com/django-setup/

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

## TODO
 - Eval the usage of ```from django.http import JsonResponse```