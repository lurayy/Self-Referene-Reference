#!/bin/sh
rm db.*
rm */migrations -r 
python3 manage.py makemigrations genreref
python3 manage.py migrate