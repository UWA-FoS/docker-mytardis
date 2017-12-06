# docker-mytardis

# Deployment - Docker compose



# Development

```
$ git clone --recursive https://github.com/UWA-FoS/docker-mytardis.git mytardis
$ cd mytardis
edit Dockerfile and/or docker-compose.yml to your desired settings
$ docker-compose up -d
```

# Configuration

Configuration can be accomplished in a number of different was as circumstance dictates.

* Dockerfile
* docker-compose.yml
* docker-entrypoint.d/
* docker-entrypoint_celery.d/
* env.MODULE
* settings.d/

# env.MODULE files

env_template.MODULE templates are provided

# References

[Django docker container](https://github.com/GoHiTech/docker-django)

