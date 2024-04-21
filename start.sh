#!/bin/sh
set -e

# Run Alembic migrations
echo "Run Alembic Migrations..."
alembic -c ./src/alembic.ini upgrade head

# Start the application
echo "Starting the application..."
uvicorn src.app.main:app --host 0.0.0.0 --port $PORT
