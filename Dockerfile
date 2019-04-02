FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD ./src /src
RUN pip install -r urbvan/requirements/base.txt
