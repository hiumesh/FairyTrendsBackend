FROM python

RUN pip install --upgrade pip

RUN pip install Django psycopg2 djangorestframework drf-writable-nested django-cors-headers

WORKDIR /app

ENTRYPOINT [ "python", "manage.py" ]