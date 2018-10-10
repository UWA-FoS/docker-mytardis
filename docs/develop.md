h1. Development

h2. Setup

[Docker installation CentOS7](https://docs.docker.com/install/linux/docker-ce/centos/)
[Compose installation](https://docs.docker.com/compose/install/)
[Compose command completion installation](https://docs.docker.com/compose/completion/)

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

