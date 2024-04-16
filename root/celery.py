from __future__ import absolute_import , unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','root.settings')

app = Celery('root')
app.conf.enable_utc = False

app.conf.update(timzone = "Asia/Karachi")

app.config_from_object(settings,namespace='CELERY')

# Celery Beat settings
    # TODO

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.requesr!r}")