web: gunicorn config.wsgi:application
worker: celery worker --app=plateiq.taskapp --loglevel=info
