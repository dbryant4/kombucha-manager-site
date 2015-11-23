FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /kombucha-manager-site
WORKDIR /kombucha-manager-site
ADD . /kombucha-manager-site/

RUN pip install -r requirements.txt
RUN pip install honcho
RUN apt-get update
RUN apt-get -y install nodejs npm
RUN apt-get -y autoremove
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install -g bower
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN python manage.py bower install --no-color
RUN python manage.py compress --force
RUN python manage.py collectstatic --no-color --noinput

CMD ["honcho", "start"]

EXPOSE 5000
