from macrosurl import url

import todos.views as todos_views


app_name = 'todos'

urlpatterns = [
    url(r'^$', todos_views.todos, name="index"),
    url(r'^:todo_id/$$', todos_views.todo, name="view"),
]
