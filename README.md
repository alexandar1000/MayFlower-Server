# MayFlower-Server

The project uses [Django](https://docs.djangoproject.com/en/3.0/) and [Django REST Framework](https://www.django-rest-framework.org/) frameworks. Please look at the documentation and best practices before beginning the development. Furthermore, the project uses [PostgreSQL](https://www.postgresql.org/) as the database. In order to start it, run the `docker-compose up` and wisit `localhost:8080` for the [Adminer](https://www.adminer.org/) administrator dashboard of the database. The database itself can be reached at `localhost:5432`, but has already been set up within the project. 


## Useful to know

In case you use requests other than GET without a trailing slash, Django will redirect the request to an address with one, but it might not be the same Http verb. E.g. `DELETE to url/user/42` will be redirected to `GET to url/user/42/`
