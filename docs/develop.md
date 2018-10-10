# Development

## Setup
* [Docker installation CentOS7](https://docs.docker.com/install/linux/docker-ce/centos/)
* [Compose installation](https://docs.docker.com/compose/install/)
* [Compose command completion installation](https://docs.docker.com/compose/completion/)

Instructions taken from above links 26/09/2018; use the above links for the most up to date instructions.
```bash
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce
sudo usermod -aG docker $USER
```

log out and back in to add the docker group into your active session
```bash
docker run hello-world

sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
sudo curl -L https://raw.githubusercontent.com/docker/compose/1.22.0/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose
```

[Compose file reference](https://docs.docker.com/compose/compose-file/compose-file-v2/)

* YAML
* Version 2.2 (why not version 3?)
* Named volumes
* Services
* Ports

For non-root access to development. This ensures that containers running with root privileges that create files can be maintained by the users account permissions on the host.
```bash
setfacl -R -m d:u:${USER}:rwX ${HOME}
setfacl -R -m u:${USER}:rwX ${HOME}
```

Ensure directories and especially files are created prior to the docker run process. Docker will create a directory on the host for any volume referenced if it does not already exist.
```docker-compose.yml
version '2.2'

volumes:
  db:
  local_directory:
    driver: local
    driver_opts:
      type: 'none'
      o: 'bind'
      device: '/path/to/local/directory'

services:
  django:
    image: uwaedu/mytardis_django:uwa.3.9.0
    build: .
    ports:
      - '8000:8000'
    environment:
      - DJANGO_DEBUG=True
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=trudatdb
      - POSTGRES_USER=trudatuser
    mem_limit: 1g
    volumes:
      - ./src/mytardis/tardis/tardis_portal/tasks.py:/usr/src/app/tardis/tardis_portal/tasks.py
  db:
    image: postgres:9.5
    environment:
      - POSTGRES_INITDB_ARGS=--data-checksums --locale=en_US.utf8
      - PGDATA=/var/lib/postgresql/data/pgdata
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=trudatdb
      - POSTGRES_USER=trudatuser
    mem_limit: 1g
    volumes:
      - db:/var/lib/postgresql/data
```
```bash
docker-compose pull
docker-compose up -d
docker-compose logs --no-color -f [<container_name>]
```

## working on code
```bash
git clone --recursive https://github.com/UWA-FoS/docker-mytardis.git
cd docker-mytardis
```
```bash
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean
```
This will clone the MyTardis Docker develoment environment and using the '--recursive' switch the upstream source code will be cloned into the src/ directory using [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules). Care needs to be taken, in that, the git submodules will be cloned in a state called 'Detached Head', to work on this code and submit to the upstream code base you should firstly read the 'Working on a Submodule' section of the referenced documentation.

```bash
cd src/mytardis
```

cat ./.gitmodule
```
[submodule "src/mytardis"]
        path = src/mytardis
        url = https://github.com/mytardis/mytardis.git
        branch = develop
[submodule "src/mydata"]
        path = src/mydata
        url = https://github.com/mytardis/mytardis-app-mydata.git
[submodule "src/nifcert"]
        path = src/nifcert
        url = https://github.com/UWA-FoS/mytardis-nifcert.git
```
```bash
rm -rf .git/modules/src/mytardis
rm -rf src/mytardis
git submodule sync
git submodule update --init --recursive --remote
cd src/mytardis
git checkout develop
```
If development is not against the MyTardis upstream development branch or this is for building a particulat tagged release.
```bash
git fetch --all --tags --prune
git checkout tags/v3.9.0 -b v3.9.0
```
```bash
cp env_template.POSTGRES env.POSTGRES
docker-compose pull
docker pull uwaedu/mytardis_django
docker-compose build
docker-compose up -d
docker-compose logs --no-color -f
```
