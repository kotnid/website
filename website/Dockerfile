FROM python:3.9-buster as production

ENV PYTHONUNBUFFERED = 1
WORKDIR /app/ 

COPY requirement.txt ./requirement.txt
RUN pip install -r ./requirement.txt

COPY manage.py ./manage.py
COPY setting.py ./setup.cfg
COPY website ./website/website

EXPOSE 8000