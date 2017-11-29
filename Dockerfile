#FROM gohitech/django:djcelery
FROM dockerdjango_django:latest
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

RUN pip install --no-cache-dir \
  psycopg2

RUN pip install --no-cache-dir -r tardis/apps/publication_forms/requirements.txt

# mytardis-app-mydata
# https://github.com/mytardis/mytardis-app-mydata
COPY src/mydata ./tardis/apps/mydata/
RUN pip install --no-cache-dir -r ./tardis/apps/mydata/requirements.txt

#RUN pip install --no-cache-dir -r tardis/apps/push_to/requirements.txt

# MyTardis LDAP authentication
RUN pip install --no-cache-dir \
  python-ldap==2.4.45

# Bioformats
# https://github.com/keithschulze/mytardisbf
RUN apt-get update && apt-get -y install \
  openjdk-7-jdk \
  && apt-get clean
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64
RUN  pip install -U --no-cache-dir \
    numpy
RUN pip install --no-cache-dir -e git+https://github.com/keithschulze/mytardisbf.git@0.1.1#egg=mytardisbf
ENV MYTARDIS_BIOFORMATS_ENABLE='False'

# https://pypi.python.org/pypi/django-generate-secret-key/1.0.2
RUN pip install --no-cache-dir \
  django-generate-secret-key==1.0.2

COPY docker-entrypoint.d/ /docker-entrypoint.d/

COPY settings.d/ ./settings.d/

ENV MYTARDIS_DEFAULT_INSTITUTION='The University of Western Australia'

ENV MYTARDIS_MYTARDIS_VERSION="{'commit_id': '6589ed8a7776deb3e7b4dec1afacfb4f405939a6', 'date': 'Mon, 13 Nov 2017 17:15:51 +0800', 'tag': '', 'branch': 'master'}"
