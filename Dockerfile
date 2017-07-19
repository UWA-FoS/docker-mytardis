FROM dockerdjango_django
MAINTAINER Dean Taylor <dean.taylor@uwa.edu.au>

ENV DJANGO_PROJECT_NAME="tardis"

RUN apt-get update && apt-get -y install \
  libfreetype6-dev \
  libjpeg-dev \
  libldap2-dev \
  libsasl2-dev \
  libssl-dev \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev \
  && apt-get clean

RUN pip install --no-cache-dir \
  anyjson==0.3.3 \
  beautifulsoup4==4.6.0 \
  billiard==3.5.0.3 \
  feedparser==5.2.1 \
  flexmock==0.10.2 \
  html5lib==0.999999999 \
  httplib2==0.10.3 \
  ipython==2.4.1 \
  pycrypto==2.6.1 \
  pystache==0.5.4 \
  python-dateutil==2.6.1 \
  PyYAML==3.12 \
  Wand==0.4.4

COPY src/mytardis/tardis/ tardis/
COPY src/mytardis/wsgi.py tardis/
COPY src/mytardis/mytardis.py ./

RUN ln -s mytardis.py manage.py

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir django-celery

COPY settings.py tardis/settings.d/
COPY docker-entrypoint.d/ docker-entrypoint.d/
