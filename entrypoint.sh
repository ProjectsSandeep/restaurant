#!/bin/bash

# Run migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Seed Database
python3 manage.py loaddata menus.json
python3 manage.py loaddata menu_items.json
python3 manage.py loaddata testimonials.json

# Collect static files
python3 manage.py collectstatic --noinput

# Run the specified command (if any)
exec "$@"