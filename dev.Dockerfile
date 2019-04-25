#
# Docker image for Django project
#
FROM python:3.7

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

# Install some OS requirements
RUN apt-get update && \
    apt-get install -yq --no-install-recommends \
    postgresql-client dos2unix build-essential && \
    rm -rf /var/lib/apt/lists/*

ENV app /usr/src/app/
ENV ops /usr/src/ops/

# Copying deployment files
WORKDIR $ops
COPY requirements/base.txt .
COPY requirements/development.txt .
COPY deployment/uwsgi.ini .
COPY deployment/docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

RUN pip install -r development.txt

# Copying project files
WORKDIR $app
COPY server .
