import os
from celery import Celery


# set the deafult Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoshop.settings')

app = Celery('djangoshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()