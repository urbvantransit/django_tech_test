FROM ubuntu:18.04

MAINTAINER Dockerfiles

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
    rm -rf /var/lib/apt/lists/*

# install uwsgi
RUN pip3 install uwsgi

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/sites-available/django_tech_test
COPY supervisor.conf /etc/supervisor/conf.d/

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.

COPY urbvan/requirements/base.txt /home/docker/django_tech_test/urbvan/requirements/base.txt
RUN pip3 install -r /home/docker/django_tech_test/urbvan/requirements/base.txt

# Copy the django_tech_test source code
COPY . /home/docker/django_tech_test/

#
#EXPOSE 80
#
#CMD ["supervisord", "-n"]
EXPOSE 8000
CMD ["python", "/home/docker/django_tech_test/manage.py", "runserver", "0.0.0.0:8000"]