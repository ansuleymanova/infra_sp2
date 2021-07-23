# api_yamdb
## Description
This study project is a knock-off of IMDB for books, movies, and songs. The titles are managed by administator, users can add reviews, rate titles and comment on the reviews of other users. The project is split into 3 separate apps: ```users```, ```titles```, and ```reviews```. 
## Technologies
The project is based on Django REST API framework and uses PostgreSQL and nginx. 
## User Manual
The repo contains files necessary to build the Docker container on your machine. Clone the repo and from the directory that contains ```docker-compose.yaml``` file run following commands:
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

The server is up, go ahead and try 127.0.0.1/admin
