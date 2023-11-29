FROM python:3.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN pip install gunicorn

COPY . /app/

COPY .env /app/.env
RUN chmod +x /app/.env

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "factorialtask.wsgi:application"]
