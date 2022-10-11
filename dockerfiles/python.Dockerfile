FROM python

RUN pip install --upgrade pip

RUN pip install Django psycopg2 djangorestframework

WORKDIR /app

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]