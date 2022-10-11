FROM python

RUN pip install --upgrade pip

RUN pip install Django psycopg2 djangorestframework

WORKDIR /app

ENTRYPOINT [ "python", "manage.py" ]