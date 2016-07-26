from __future__ import unicode_literals

from django.db import models
import datetime


class Event(models.Model):
    name = models.CharField(max_length=45)
    date = models.DateField()
    start_time = models.TimeField(default=datetime.time(hour=0, minute=0))
    end_time = models.TimeField(blank=True, null=True)
    notes = notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
