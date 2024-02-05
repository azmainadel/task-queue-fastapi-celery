import os

from celery import Celery
from constant.urls import BACKEND_URL, BROKER_URL

celery_app = Celery(
    "worker",
    backend=BACKEND_URL,
    broker=BROKER_URL
)
celery_app.conf.task_routes = {
    "app.app.worker.celery_worker.test_celery": "test-queue"}

celery_app.conf.update(task_track_started=True)
