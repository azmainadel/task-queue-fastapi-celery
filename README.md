## Task Queue using FastAPI-Celery-RabbitMQ

* FastAPI and Celery with RabbitMQ for task queue
* Redis as Celery backend
* Flower as task monitor

## Requirements

- Docker
  - [docker-compose](https://docs.docker.com/compose/install/)

## Run Guide

1. Run ```docker-compose up``` to start up the instances.
2. Visit [http://localhost:8000/docs](http://localhost:8000/docs) to execute test task API calls. 
3. Monitor the execution of the celery tasks at [http://localhost:5555](http://localhost:5555) (username: test, password: dummypass1234).
