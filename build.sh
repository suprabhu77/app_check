#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

# Run Django collectstatic to gather static files
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput

# Run migrations
echo "Running migrations..."
python3.9 manage.py makemigrations
python3.9 manage.py migrate