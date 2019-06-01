from django.db import models
from django.utils import timezone


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(TimestampModel):
    name = models.CharField(max_length=100, default="")

    start_time = models.DateTimeField(default=timezone.now())
    required_hours = models.PositiveIntegerField(default=1)
