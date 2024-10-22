# Simple flask-unity application

This is a simple flask-unity application that can be run locally, also it is decorise using docker container. The content of the `docker-compose.yml` file is:

```yml
version: '3.7'
services:
    fu_service:
        build:
            context: .
        ports:
            - "7000:7000"
```

save the file and spinup the services, by runing the command below::

```sh
docker-compose up
```

you can use the command below instead of the above, in other to see how it build the image::

```sh
docker-compose up --build
```

Once the services build up, you can visit it at `http://0.0.0.0:7000`


<!-- 
pip install --upgrade flask_unity

flaskunity -p schoolsite

cd schoolsite

flaskunity db makemigrations

flaskunity db migrate

python3 run.py boot --port 7000 --debug True --host 0.0.0.0
 -->

## To build and deploy to docker-hub

```sh
docker image build -t usmanmusa/flask-unity-app .

docker logout # or docker login -u <username>
docker login

docker image push usmanmusa/flask-unity-app
```
