from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .models import *
from django.views.generic import *
from django.utils import timezone


def home(request):
    events = Event.objects.exclude(date__lt=datetime.date.today()).order_by("start_time").order_by("date")
    events_today = Event.objects.filter(date=datetime.date.today()).order_by("start_time")
    events_future = Event.objects.exclude(date__lte=datetime.date.today()).order_by("start_time").order_by("date")
    now = timezone.localtime(timezone.now())

    ticker_list = []

    for event in events_today:
        if now.hour < event.start_time.hour:                                                # hours before start time
            hour_difference = event.start_time.hour - now.hour
            if hour_difference == 1:
                minute_difference = event.start_time.minute + 60 - now.minute
                ticker_list.append("in %s minutes" % minute_difference)
            else:
                ticker_list.append("in %s hours" % hour_difference)
        if now.hour == event.start_time.hour:                                               # same hour as start time
            minute_difference = now.minute - event.start_time.minute
            if minute_difference < 0:
                ticker_list.append("in %s minutes" % abs(minute_difference))
            else:
                if event.end_time is None:
                    ticker_list.append("started %s minutes ago" % minute_difference)
                else:
                    end_minute_difference = now.minute - event.end_time.minute
                    end_hour_difference = now.hour - event.end_time.hour
                    if end_hour_difference > 0 or end_minute_difference < 0:
                        ticker_list.append("happening now")
                    else:
                        ticker_list.append("ended %s minutes ago" % end_minute_difference)
        if now.hour > event.start_time.hour:                                                # hours after start time
            hour_difference = now.hour - event.start_time.hour
            if event.end_time is None:
                if hour_difference == 1:
                    minute_difference = now.minute + 60 - event.start_time.minute
                    ticker_list.append("started %s minutes ago" % minute_difference)
                else:
                    events = events.exclude(id=event.id)
            else:
                end_hour_difference = now.hour - event.end_time.hour
                if end_hour_difference > 1:
                    events = events.exclude(id=event.id)
                if end_hour_difference < 0:
                    ticker_list.append("happening now")
                else:
                    end_minute_difference = now.minute + 60 * end_hour_difference - event.end_time.minute
                    if end_minute_difference <= 0:
                        ticker_list.append("happening now")
                    else:
                        ticker_list.append("ended %s minutes ago" % end_minute_difference)

    for event in events_future:
        today = datetime.date(now.year, now.month, now.day)
        days_difference = (event.date - today).days
        ticker_list.append("in %s days" % days_difference)

    events_ticker = zip(events, ticker_list)

    context = {
        'events_ticker': events_ticker,
    }

    return render(request, "home.html", context)


class EventAdd(CreateView):
    model = Event
    success_url = reverse_lazy('ticker:home')
    fields = ['name', 'date', 'start_time', 'end_time', 'notes']
