# django-travel
Route selection web application

## Environment

In the project folder create file `.env` and set values for environment:

```
DEBUG=1
SECRET_KEY=yor_secret_key
SQL_ENGINE=postgresql
SQL_DATABASE=your_db_name
SQL_USER=your_user
SQL_PASSWORD=your_password
SQL_HOST=db
SQL_PORT=5432
```

## Use via Docker

On the command line, run `cd yor_project_path`

### Start

`docker-compose up -d`

### Stop

`docker-compose down`

### Rebuild

1. `docker-compose down -v --remove-orphans`
2. `docker-compose rm -vsf`
3. `docker-compose up -d --build`

Open [http://localhost:8000](http://localhost:8000) in your browser
