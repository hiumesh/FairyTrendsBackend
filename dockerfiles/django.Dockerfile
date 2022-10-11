FROM python

RUN pip install --upgrade pip

RUN pip install Django psycopg2 djangorestframework

WORKDIR /app

# CMD [ "django-admin", "startproject", "FairyTrends", "." ]
ENTRYPOINT [ "django-admin" ]