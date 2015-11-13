FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /kombucha-manager-site
WORKDIR /kombucha-manager-site
ADD . /kombucha-manager-site/
RUN pip install -r requirements.txt
