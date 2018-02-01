# Simple Web-service to send email notifications

## Development

### Install

You should have `git` and `docker` previously installed

```sh
git clone https://github.com/1d20/EmailNotificationWebService.git
cd EmailNotificationWebService/
docker-compose up --build
```

### Create superuser

```sh
docker-compose exec web python manage.py createsuperuser
```

### Create migrations

```sh
docker-compose exec web python manage.py makemigrations
```
