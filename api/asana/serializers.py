from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField

from asana.models import Task


class TaskUrlHyperlinkedRelatedField(HyperlinkedIdentityField):
    def __init__(self, **kwargs):
        super(TaskUrlHyperlinkedRelatedField, self).__init__(
            'asana:tasks:view',
            lookup_url_kwarg='task_id'
        )


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    serializer_url_field = TaskUrlHyperlinkedRelatedField

    class Meta:
        model = Task
        fields = ('name', 'start_time', 'required_hours', 'url')
