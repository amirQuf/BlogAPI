# Pull base image
FROM  python:3.7

# Set environment variables

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#SET WORK DIRECTROY
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/


