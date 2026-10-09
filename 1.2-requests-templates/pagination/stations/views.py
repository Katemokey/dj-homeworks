import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def load_bus_stations():
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
        return list(csv.DictReader(file))


def bus_stations(request):
    paginator = Paginator(load_bus_stations(), 10)
    page = paginator.get_page(request.GET.get('page'))

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
