FROM python:3.8.0

WORKDIR /app

COPY ./requirements.txt requirements.txt

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput


CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
