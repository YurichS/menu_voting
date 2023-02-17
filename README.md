# Rest API for voting menus
## How to run the system:

1. Build the image and run the conteiner.
>``` $ docker-compose up -d --build```

2. Create migrations.
```
$ docker-compose exec web python manage.py makemigrations 
$ docker-compose exec web python manage.py migrate
```
3. Test it on `localhost:8000`

