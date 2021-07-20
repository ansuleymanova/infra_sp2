# api_yamdb
## Description
This study project is a knock-off of IMDB for books, movies and songs.
## User Manual
In terminal, from the directory that contains '''docker-compose.yaml''' run following commands:
### Startup
```
docker-compose up --build -d
docker-compose exec web python manage.py makemigrations users
docker-compose exec web python manage.py makemigrations titles
docker-compose exec web python manage.py makemigrations reviews
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input
```
### Superuser
```docker-compose exec web python manage.py createsuperuser```
### Fixtures
```docker-compose exec web python manage.py loaddata fixtures.json```
