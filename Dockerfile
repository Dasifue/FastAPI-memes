FROM python:3.12-alpine

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    netcat-openbsd

RUN pip install --upgrade pip
ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . .


COPY wait-for-db.sh /app/wait-for-db.sh
RUN chmod +x /app/wait-for-db.sh

CMD alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000
