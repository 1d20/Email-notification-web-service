# Simple Web-service to send email notifications

## Demo

 - **Server**: http://18.216.38.56:8001/
 - **Username**: test
 - **Password**: test_test_42

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
