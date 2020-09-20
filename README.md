# MayFlower-Server

The project uses [Django](https://docs.djangoproject.com/en/3.0/) and [Django REST Framework](https://www.django-rest-framework.org/) frameworks. Please look at the documentation and best practices before beginning the development. Furthermore, the project uses [PostgreSQL](https://www.postgresql.org/) as the database. In order to start it, run the `docker-compose up` and wisit `localhost:8080` for the [Adminer](https://www.adminer.org/) administrator dashboard of the database. The database itself can be reached at `localhost:5432`, but has already been set up within the project. 


## Useful to know

In case you use requests other than GET without a trailing slash, Django will redirect the request to an address with one, but it might not be the same Http verb. E.g. `DELETE to url/user/42` will be redirected to `GET to url/user/42/`


## Getting started with development
0. Run the docker instance with `docker-compose up`
1. In another terminal, create an venv in the project root with `python3 -m venv venv`
2. `cd mayflower_server`
3. Copy the `.env-example` file and rename it to `.env`
4. Adjust the environment values as needed
5. From the root folder, start the venv with:
 
    `source venv/bin/activate` (Linux/Mac)
    
    `venv\scripts\activate` (Windows)
6. Install the required dependancies with `pip install -r requirements.txt`.
7. You are ready for development

### Important
Change the environment values only in the `.env` file and not in the project `settings.py` file; they will automatically be updated this way.

### Endpoints Supported
The server will run on localhost:8000 by default.
#### Battery
+ GET /api/v1/battery/   [Get the whole list of battery]
+ GET /api/v1/battery/<int: battery_id>/ [Get a single battery by id]
+ POST /api/v1/battery/ [Create new battery with 'application/json' as content_type]
+ PUT /api/v1/battery/<int: battery_id>/ [Update a single battery by id]
+ DELETE /api/v1/battery/<int: battery_id>/ [Delete a single battery by id]

#### Distance


#### GPS
+ GET /api/v1/gps/   [Get the whole list of all GPS records]
+ GET /api/v1/gps/<int: gps_id>/ [Get a single GPS by id]
+ POST /api/v1/gps/ [Create new GPS record with 'application/json' as content_type]
+ PUT /api/v1/gps/<int: gps_id>/ [Update a single GPS record by id]
+ DELETE /api/v1/gps/<int: gps_id>/ [Delete a single GPS by id]

#### 3D Lidar

#### IMU

#### Thermometer

#### Video Image

#### Controls