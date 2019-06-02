from __future__ import absolute_import

import os
from celery import Celery


settings = dict(
    dev='vocdjango.settings',
    test='vocdjango.settings.test',
    prod='vocdjango.settings.prod'
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings.get(os.environ.get('VOC_DJANGO_ENV', 'dev')))


app = Celery('voc_django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
