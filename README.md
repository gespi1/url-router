Run Local Postgres
```
docker run --rm --name db -e POSTGRES_PASSWORD=test -e PGDATA=/var/lib/postgresql/data/pgdata -v $HOME/github/url-router/db:/var/lib/postgresql/data -p 5432:5432 -d postgres
```