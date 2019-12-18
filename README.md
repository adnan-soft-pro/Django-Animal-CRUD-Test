# Overview

This is very simple test task to check specific skills like Django and Django REST framework.

# Quick start

  - Install all packages from requirements.txt
```sh
   $ pip install -r requirements.txt
```
  - Migrate app, create superuser and run project.
```sh
   $ python manage.py migrate
   $ python manage.py createsuperuser
   $ python manage.py runserver
```
  - Project will run on http://127.0.0.1:8000/
  
# API Information

/ Request Method | Endpoints | Description |
| ------ | ------ | ------ |
| GET | /api/list/ | Show the list of pets |
| POST | /api/create/ | Create a new pet|
| PUT | /api/edit/\<id\>/ | Update a pet specified by id |
| DELETE | /api/edit/\<id\>/ | Delete a pet specified by id |
