import os
from celery import Celery
from core.task import update_pujo_scores, backup_logs_to_minio
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('DJANGO_SETTINGS_MODULE'))

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.register_task(update_pujo_scores)
app.register_task(backup_logs_to_minio)

app.conf.broker_connection_retry_on_startup = True
app.conf.task_time_limit = 300 