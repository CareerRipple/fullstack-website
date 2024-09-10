FROM python:3.11-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache --upgrade pip

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache -r requirements.txt
#RUN pip install --no-cache gunicorn

COPY . .

COPY ./entrypoint.sh .
ENTRYPOINT [ "sh","/app/entrypoint.sh" ]