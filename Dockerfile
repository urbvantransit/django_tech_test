#!/bin/bash
# Descargamos la imagen base oficial de python y linux
FROM python:3.6-alpine
# Definimos unas variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Creamos el directorio donde se contendrá el proyecto
RUN mkdir /usr/src/app
# Seleccionamos el directorio sobre el cual trabajaremos
WORKDIR /usr/src/app
# Instalamos dependencias en el sistema, como postgres
# para la base de datos y demás dependencias
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps
# actualizamos el manejador de paquetes de Python PIP
RUN pip install --upgrade pip
# instalamos la mejora del manejador de paquetes
RUN pip install pipenv
# copiamos nuestro .Pipfile a nuestro WORKDIR (./code)
COPY ./Pipfile /usr/src/app
# ejecutamos el comando pipenv install, para instalar
# todas las dependencias de nuestro .Pipfile
RUN pipenv install --skip-lock --system --dev
# copiamos entrypoint a ./code dentro de docker
COPY entrypoint.sh /usr/src/app
# ejecutamos entrypoint
RUN chmod +x /usr/src/app/entrypoint.sh
# copiamos todo lo que esté en la raiz de nuestro proyecto raíz
# a ./code en django
COPY . /usr/src/app
# punto de entrada
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]