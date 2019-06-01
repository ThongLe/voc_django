from macrosurl import url
from django.conf.urls import include

from rest_framework import routers

from .asana.views import TaskViewSet


app_name = 'api'

asana_router = routers.DefaultRouter()
asana_router.register(r'tasks', TaskViewSet)


urlpatterns = [
    url(r'^asana/$', include(asana_router.urls)),
]
