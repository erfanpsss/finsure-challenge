# finsure-challenge

This is a simple Django app which provides functionality creating, updating, deleting, listing, and retrieving 
Lender records through Rest API. 

Installation

Requires python 3

1- Run "python -m pip install -r requirements.txt"

2- Clone .env-example and rename it to .env and change the env variables based on you db configuration

3- Run "python manage.py migrate"

4- Run "python manage.py collectstatic"

5- Run developement server using "python manage.py runserver"