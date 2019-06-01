from macrosurl import url
from django.conf.urls import include

from . import views as asana_views


app_name = 'asana'

tasks_urlpatterns = [
    url(r'^$', asana_views.list_tasks, name="index"),
    url(r'^create/$', asana_views.create_task, name="create"),
    url(r'^:task_id/$$', asana_views.view_task, name="view"),
]

urlpatterns = [
    url(r'^tasks/$', include((tasks_urlpatterns, 'tasks'), namespace='tasks')),
]
