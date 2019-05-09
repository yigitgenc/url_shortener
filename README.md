# URL Shortener API

A minimal dockerized URL shortener API.

###  Contents

1. [Installing](#installing)
2. [Running Tests](#running-tests)
3. [Using the API](#using-the-api)
4. [Project Structure](#project-structure)

### Installing

Before building and running the services;
let's create `.env` file in order to set environment variables.
```bash
echo "
APP_HOST=0.0.0.0
APP_PORT=8000

FLASK_APP=app
FLASK_ENV=development

SECRET_KEY=VerySecretKey
" > .env
```
> `.env` file must be created in the top-most directory
(along with `docker-compose.yml`).

Now we can build the app image and start the services.
```bash
docker-compose build
docker-compose up -d
```

### Running Tests

You can easily run the tests by running:
```bash
docker-compose run --rm app pytest --verbose --cov=.
```

### Using the API

##### Redirect Endpoint *[/<string:code> (GET)]*
```bash
curl -v -X GET http://localhost:8000/<string:code>
```

##### Shortening URL Endpoint *[/shorten (POST)]*
```bash
curl -v -X POST -d url=http://example.com http://localhost:8000/shorten
```



### Project Structure

```bash
├── Dockerfile
├── README.md
├── app
│   ├── app
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── settings.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── pytest.ini
│   ├── requirements.txt
│   └── tests
│       ├── __init__.py
│       ├── test_utils.py
│       └── test_views.py
├── docker-compose.override.yml
└── docker-compose.yml
```
