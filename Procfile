web: python manage.py collectstatic --noinput; python manage.py run_gunicorn -b 0.0.0.0:$PORT -w 3 --max-requests 250 --preload