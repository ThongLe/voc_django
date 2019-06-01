from macrosurl import url

import todos.views as todos_views


app_name = 'todos'

urlpatterns = [
    url(r'^$', todos_views.list_tasks, name="index"),
    url(r'^create/$', todos_views.create_task, name="create"),
    url(r'^:task_id/$$', todos_views.view_task, name="view"),
]
