FROM python:3.9.2-slim as production

ENV PYTHONUNBUFFERED = 1
WORKDIR /app/ 

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev

COPY requirement.txt ./requirement.txt
RUN pip install -r ./requirement.txt

COPY manage.py ./manage.py
COPY website ./website/website

EXPOSE 8000

FROM production as development 

COPY . .