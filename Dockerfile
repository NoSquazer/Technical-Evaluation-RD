FROM python:3.10.5-slim-buster

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

RUN chmod +x /usr/src/app/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/bin/sh","/usr/src/app/entrypoint.sh"]
