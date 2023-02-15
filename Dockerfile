FROM python:3.10-alpine AS build-python
RUN apk update && apk add --virtual build-essential gcc python3-dev musl-dev postgresql-dev linux-headers g++
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY ./requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV PATH="/opt/venv/bin:$PATH"

COPY --from=build-python /opt/venv /opt/venv
RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev postgresql-dev
RUN pip install psycopg2-binary
WORKDIR /app
RUN chmod -R 777 /app

COPY . .
RUN python manage.py collectstatic --noinput
RUN adduser -D myuser

RUN chown myuser:myuser /app
RUN chown myuser:myuser /app/db.sqlite3

USER myuser
CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT




