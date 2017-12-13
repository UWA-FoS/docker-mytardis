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

# push_to
RUN pip install --no-cache-dir \
  -r tardis/apps/push_to/requirements.txt

# Bioformats workaround
# Fix schema check migration timing issue; Bioformats fixture loaded in /docker-entrypoint.d/mytardisbf
COPY ./src/mytardisbf_apps.py /usr/src/app/src/mytardisbf/mytardisbf/apps.py

COPY docker-entrypoint.d/ /docker-entrypoint.d/
COPY docker-entrypoint_celery.d/ /docker-entrypoint_celery.d/

COPY settings.d/ ./settings.d/

ENV MYTARDIS_DEFAULT_INSTITUTION='The University of Western Australia'

ENV MYTARDIS_MYTARDIS_VERSION="{'commit_id': '0a75a1310e08f28dfa575a23c1da6d0f46e7672a', 'date': 'Thu, 3 Nov 2016 12:22:24 +1100', 'tag': '3.7.8', 'branch': 'HEAD'}"
