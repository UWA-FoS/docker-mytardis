# docker-mytardis

# Deployment - Docker compose



# Development

```
$ git clone --recursive https://github.com/UWA-FoS/docker-mytardis.git mytardis
$ cd mytardis
```

* rename the relevant env_template.MODULE file removing the "_template" from the name.
* edit the env.MODULE files with the required settings.
* template file that are not required, ensure the files are renamed and blank OR remove the relevant entry in the docker-compose.yml file.
* edit Dockerfile and/or docker-compose.yml to your desired settings / alterations.


```
$ docker-compose up -d
```

This development uses [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to incorporate other code bases into the build process were appropriate, such as the MyTardis source. To work on a different upstream version you should follow "Working on a Project with Submodules", "Pulling in Upstream Changes". E.g.,

```
To pull the latest upstream changes from MyTardis.
From the cloned project directory run
$ cd src/mytardis
$ git fetch
$ git merge origin/master
$ cd ../..
$ docker-compose build
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

