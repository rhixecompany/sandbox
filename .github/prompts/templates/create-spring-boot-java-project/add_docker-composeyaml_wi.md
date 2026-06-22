# Add `docker-compose.yaml` with Redis, PostgreSQL and MongoDB services

> Extracted from `create-spring-boot-java-project.prompt.md`.

## Add `docker-compose.yaml` with Redis, PostgreSQL and MongoDB services

- Create `docker-compose.yaml` at project root and add following services: `redis:6`, `postgresql:17` and `mongo:8`.
  - redis service should have
    - password `rootroot`
    - mapping port 6379 to 6379
    - mounting volume `./redis_data` to `/data`
  - postgresql service should have
    - password `rootroot`
    - mapping port 5432 to 5432
    - mounting volume `./postgres_data` to `/var/lib/postgresql/data`
  - mongo service should have
    - initdb root username `root`
    - initdb root password `rootroot`
    - mapping port 27017 to 27017
    - mounting volume `./mongo_data` to `/data/db`
