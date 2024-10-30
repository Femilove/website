set -o errexit

ENTRYPOINT [ "gunicorn" , "school.wsgi"
pip install -r requirements.txt
pip install gunicorn

python manage.py collectstatic 
python manage.py migrate
