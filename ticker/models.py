from __future__ import unicode_literals

from django.db import models
import datetime

class Event(models.Model):
    name = models.CharField(max_length=45)
    date = models.DateField()
    start_time = models.TimeField(default=datetime.time(hour=0, minute=0))
    end_time = models.TimeField(blank=True, null=True)
    notes = notes = models.TextField(blank=True, null=True)

    def clean(self):
        start_t = self.cleaned_data.get("start_time")
        end_t = self.cleaned_data.get("end_time")

        if end_t and end_t < start_t:
            msg = u"End time should be greater than start time."
            self._errors["end_time"] = self.error_class([msg])