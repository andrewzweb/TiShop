# base image 
FROM python:3.8

# File Author / Maintainer
MAINTAINER Esther

# Copy the application folder inside the container
ADD . /usr/src/app

# set the default directory where CMD will execute
WORKDIR /usr/src/app

COPY deploy/requirements.txt ./

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8000

# default command to execute    
CMD exec gunicorn -w 3 -b 0.0.0.0:8000 --chdir base_app/ base_app.wsgi:application --reload

 
