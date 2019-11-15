FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Create folder for code
RUN mkdir /code

# Set the work directory
WORKDIR /code

# Add the requirements file
ADD urbvan/requirements/base.txt /code/

# Install dependencies
RUN pip3 install -r base.txt

# Add the code
ADD . /code/

# Run migrations and start server
CMD python manage.py migrate
CMD python manage.py run test
CMD python manage.py runserver 0.0.0.0:8000 --settings=urbvan.settings.base
EXPOSE 8000

