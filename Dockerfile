FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD ./src /src
RUN pip install -r urbvan/requirements/base.txt
RUN pip install uwsgi

ENV DJANGO_ENV=local
ENV DOCKER_CONTAINER=1
EXPOSE 8000
CMD ["uwsgi", "--ini", "/src/uwsgi.ini"]
