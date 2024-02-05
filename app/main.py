import os
import logging

from threading import Thread
from fastapi import FastAPI, BackgroundTasks
from worker.celery_app import celery_app

log = logging.getLogger(__name__)

app = FastAPI()


def celery_on_message(body):
    log.warn(body)

def background_on_message(task):
    log.warn(task.get(on_message=celery_on_message, propagate=False))


@app.get("/{data}")
async def root(data: str, background_task: BackgroundTasks):
    task_name = "app.app.worker.celery_worker.test_celery"

    task = celery_app.send_task(task_name, args=[data])
    print(f"Task => {task}")
    background_task.add_task(background_on_message, task)

    return {"message": "Data received"}
