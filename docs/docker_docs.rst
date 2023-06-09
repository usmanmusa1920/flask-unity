:tocdepth: 2

Sakyum on docker
################

This repo contains code to spin up a boilerplate sakyum project with Docker Compose. To run sakyum with docker compose, first pull it by::

  docker pull usmanmusa/sakyum

Next you are to clone the github repo of the project in other to get the `docker-compose.yml` by::
  
  git clone https://github.com/usmanmusa1920/sakyum.git


Now cd into the project folder you just clone to spin up the services using the command::
  
  cd sakyum/example/sakyum_demo


To spinup the services, run the command::
  
  docker-compose up


you can use the command below instead of the above, in other to see how it build the image::
  
  docker-compose up --build


Once the services build up, you can visit it at `http://0.0.0.0:5000`, also you can login with these credentials, where username is: `backend-developer` and the password is: `123456`

# Bonus usage

Inspect volume::
  
  docker volume ls

and::

  docker volume inspect <volume name>

Prune unused volumes::
  
  docker volume prune

View networks::
  
  docker network ls

Bring services down::
  
  docker-compose down

Open a bash session in a running container::
  
  docker exec -it <container ID> sh

**Source code** for the `database migration` is available at official `github <https://github.com/usmanmusa1920/sakyum/tree/master/example/sakyum-docker>`_ repository of the project.
