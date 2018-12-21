FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Create folder for code
RUN mkdir /code

# Set the work directory
WORKDIR /code

# Add the requirements file
ADD urbvan/requirements/base.txt /code/

# Copy nginx file
COPY urbvan.site.conf /etc/nginx/sites-available/

# Install dependencies
RUN pip3 install -r base.txt

# Add the code
ADD . /code/

# Run migrations and start server
CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:7000 --settings=urbvan.settings.base
EXPOSE 7000

