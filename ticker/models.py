from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

SERVER_CHOICES = (
    ('UHC1', 'Ultra Hardcore Server 1'),
    ('UHC2', 'Ultra Hardcore Server 2'),
)

class Event(models.Model):
    name = models.CharField(max_length=45)
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=datetime.time(hour=0, minute=0))
    end_time = models.TimeField(blank=True, null=True)
    server = models.CharField(choices=SERVER_CHOICES, default='UHC1', max_length=4)
    gamemode = models.CharField(default='Vanilla', max_length=100)
    team_size = models.IntegerField(default=1)
    notes = notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
