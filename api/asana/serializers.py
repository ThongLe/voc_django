from rest_framework import serializers

from asana.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'start_time', 'required_hours')
