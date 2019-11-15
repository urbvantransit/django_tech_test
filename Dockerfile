FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Create folder for code
RUN mkdir /code

# Install  GDAL library
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin

# After install PROJ.4 and GEOS install GDAL, fix versions gdal with container
#######
#RUN wget http://download.osgeo.org/gdal/1.11.2/gdal-1.11.2.tar.gz
#RUN tar xzf gdal-1.11.2.tar.gz
#RUN cd gdal-1.11.2
#RUN ./configure
#RUN make
#RUN make install
#RUN cd ..
###########

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
CMD python manage.py run test
CMD python manage.py runserver 0.0.0.0:8000 --settings=urbvan.settings.base
EXPOSE 8000

