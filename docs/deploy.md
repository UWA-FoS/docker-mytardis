```bash
./gen-mytardis_version.sh > settings.d/MYTARDIS_VERSION.py
sed -i 's;image: uwaedu/mytardis_django:.*$;image: uwaedu/mytardis_django:uwa.3.9.0;' docker-compose.yml
docker-compose build
docker login
docker tag uwaedu/mytardis_django:3.9.0 uwaedu/mytardis_django:latest
docker push uwaedu/mytardis_django:3.9.0
docker push uwaedu/mytardis_django:latest
docker logout
```
