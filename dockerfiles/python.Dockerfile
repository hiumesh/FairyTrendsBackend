FROM python

RUN pip install --upgrade pip

RUN pip install Django psycopg2 djangorestframework drf-writable-nested django-cors-headers

WORKDIR /app

CMD [ "python", "-u", "manage.py", "runserver", "0.0.0.0:8000" ]