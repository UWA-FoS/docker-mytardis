FROM gohitech/django:djcelery
#FROM dockerdjango_django:latest
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

RUN pip install --upgrade --no-cache-dir \
  pip

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

# Based on src/mytardis/build.sh
COPY requirements-base.txt src/mytardis/requirements-docs.txt src/mytardis/requirements-test.txt ./
RUN pip install --no-cache-dir \
  -r requirements-base.txt \
  -r requirements-docs.txt \
  -r requirements-test.txt
# from src/mytardis/package.json
RUN apt-get update && apt-get -y install \
  npm \
  && apt-get clean
RUN npm install \
  angular@1.3.2 \
  angular-resource@1.3.2 \
  ng-dialog@0.3.4

# UserWarning: The psycopg2 wheel package will be renamed from release 2.8
# <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>
RUN pip install --no-cache-dir \
  psycopg2-binary

# Publication forms
RUN pip install --no-cache-dir \
  -r tardis/apps/publication_forms/requirements.txt

# mytardis-app-mydata
# https://github.com/mytardis/mytardis-app-mydata
COPY src/mydata ./tardis/apps/mydata/
RUN pip install --no-cache-dir \
  -r ./tardis/apps/mydata/requirements.txt


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
COPY ./src/forms.py /usr/src/app/tardis/tardis_portal/forms.py
COPY ./src/widgets.py /usr/src/app/tardis/tardis_portal/widgets.py

COPY docker-entrypoint.d/ /docker-entrypoint.d/
COPY docker-entrypoint_celery.d/ /docker-entrypoint_celery.d/

COPY settings.d/ ./settings.d/
COPY settings_pre.py ./settings_pre.py

ENV MYTARDIS_DEFAULT_INSTITUTION='The University of Western Australia'
