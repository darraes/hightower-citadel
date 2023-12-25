## Created based on 
https://realpython.com/django-setup/

## Migrations can be refreshed using the following
python3 manage.py makemigrations citadel && python3 manage.py migrate

## Check typing
mypy -p citadel --strict --exclude "migration|apps"

## TODO
 - Eval the usage of ```from django.http import JsonResponse```