# Python Version
FROM python:3.8.3
COPY requirements.txt /tmp/
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt
COPY ./product_management_api /product_management_api
