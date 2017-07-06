FROM dockerdjango_django
MAINTAINER Dean Taylor <dean.taylor@uwa.edu.au>

ENV DJANGO_PROJECT_NAME="tardis"

COPY src/mytardis/tardis/ ./tardis/
COPY src/mytardis/wsgi.py ./tardis/
COPY src/mytardis/mytardis.py ./
RUN ln -s mytardis.py manage.py

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY settings.py ${DJANGO_PROJECT_NAME}/
