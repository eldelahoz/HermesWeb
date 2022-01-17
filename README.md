# HermesWeb

## Just one project in django.

## 🇪🇦 Español:

### Python

En este proyecto uso virtualenv para la creación del entorno virtual de Python 3.7.7 con Django a la version 3.2.8, los
demas requisitos para el proyecto estan en el archivo: [requirements.txt]

Para la creacion del entorno virtual y los requerimientos use lo siguiente:

- virtualenv -p python3.7 hermesweb
- source bin/activate
- pip install -r requeriments.txt

### Docker

<img src="https://www.docker.com/sites/default/files/d8/2019-07/vertical-logo-monochromatic.png" alt="docker-img" width="100"/>

Se utiliza docker para la gestion del servicio de base de datos, que en este caso se utiliza *Postgres*, pueden utilizar
el archivo [docker-compose.yml] para la creacion de la imagen automaticamente.

A su vez se debe ingresar al contendor para crear la base de datos en este caso db, ejemplo:
``` dockerfile
docker exec -it docker-postgres-1 bash
psql -U postgres
create database db;
```
## 🇺🇸 English:

<!-- *** The links -->

[requirements.txt]: app/requirements/requirements.txt

[docker-compose.yml]: Docker/docker-compose.yml
