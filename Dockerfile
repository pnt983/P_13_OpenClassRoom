FROM python:3.8.0

WORKDIR /app

# COPY ./requirements.txt /app/requirements.txt
COPY ./requirements.txt requirements.txt

# WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

# COPY . /app
COPY . .

CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]
# CMD uvicorn main:app --reload --host 0.0.0.0 --port 8000