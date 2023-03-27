# CreditCard Backend

Django and Django Rest API based backend system to save credit card
information.
It uses Django to manage user to provide authentication for access
to de REST API of credit cards.
It's recommended to use virtualization over Docker to avoid environment
misconfiguration and divergences between development, release and
production envs.
For this, a docker compose configuration is provided and the
intructions are base on runing on docker toolset.
Feel free to hack this code and make suggestions on how to improve
the project.

# Requirements

This project requires [Docker](https://docs.docker.com/desktop/install/linux-install/)
already installed and running on the system.

# First steps

Build docker image and initialize the database with provided
migrations.
Run the following commands:

```
# Build image and install dependencies
docker-compose -f docker/docker-compose.yaml build

# Initialize database and application
docker-compose -f docker/docker-compose.yaml up
```

Create an admin user:

```
# use docker ps to get the ID of running container
docker ps

# replace <ID> with the container ID to manage the virtual application
docker exec -it <ID> /bin/bash

# follow Django instructions to create an admin user
python manage.py createsuperuser
```

## Recommendation

It's recommendend not to use admin user to perform normal
operations on the system, due to high level of permissions.
Thus, create a normal user to access the system on the
Django Web interface:

1. Access on the web browser: `http://localhost:8000/admin` and
   use the previously created admin credentials to login on the system
2. On user form, create a user and keep the provided information
   to use as authentication for the REST API

# Acessing the REST API

There are many ways to access the CreditCard Rest API.
From GUIs, to Web Interfaces and even CLI tools.
Feel free to configure and use with the tools you like.
However, to provide general knowledge that do not rely on a certain
tool or GUI, this documentation uses plain HTTP commands to give
instructions on how to access the API.

## Authentication

The simplest secure way to provide authentication credentials is
using Basic Authentication.
For this, concatenate `<USERNAME>:<PASSWORD>` and encode using
base64 algorithym.
After this, pass the encoded credential on the Header of the
HTTP request using the key `Authorization`, i.e.:

```
Authorization: Basic <B64_ENCODED_STRING>
```

## Performing API operations

List Credit Cards saved on database:

```
GET / HTTP/1.1
Host: http://localhost:8000/api/v1/credit-card
Authorization: Basic <B64_ENCODED_STRING>
```

Create a new Credit Card:

```
POST / HTTP/1.1
Host: http://localhost:8000/api/v1/credit-card
Authorization: Basic <B64_ENCODED_STRING>
Content-Type: application/json

{
	"exp_date": <MM/DD_DATE_FORMAT>,
	"holder": <STRING>,
	"card_number": <CARD_NUMBER>,
	"cvv": <NOT_REQUIRED>
}
```

Update a givin Credit Card:

```
PUT /<ID_OF_CREDIT_CARD>/ HTTP/1.1
Host: http://localhost:8000/api/v1/credit-card
Authorization: Basic <B64_ENCODED_STRING>
Content-Type: application/json

{
	"id": <ID_OF_CREDIT_CARD>,
	"exp_date": <MM/DD_DATE_FORMAT>,
	"holder": <STRING>,
	"card_number": <CARD_NUMBER>,
	"cvv": <NOT_REQUIRED>
}
```

Developer:
[Leonardo Ramos Santos](leonardo.ramosantos@yahoo.com.br)
