from macrosurl import url

from . import views as tasks_views


app_name = 'tasks'

urlpatterns = [
    url(r'^$', tasks_views.list_tasks, name="index"),
    url(r'^create/$', tasks_views.create_task, name="create"),
    url(r'^:task_id/$$', tasks_views.view_task, name="view"),
]
