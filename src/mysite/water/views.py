from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Final
import os
import shutil
from datetime import date
import json
import requests
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
@login_required
def index(request):
    # if not request.user.is_authenticated():
        # return render(request, 'registration/login.html')
    Final.getgraph_currweek_line(Final)
    curr_yr = date.today().year - 1
    curr = date.today().replace(year = curr_yr)
    out = Final.get_by_date(Final, curr)
    nrw = out
    a, b, c = Final.get_avg_by_block(Final)
    # print("C = ", c)
    # args = {'total_consumption_by_date' : str(out)}
    # print(args)
    leakages = Final.get_leakages(Final)
    # print(leakages)
    leak = json.dumps(leakages)
    # return render(request, 'index.html', {'total_consumption_by_date' : out, 'avg_block' : c, 'nrw' : nrw, 'leakages' : leak})
    print("C = ", c)
    args = {'total_consumption_by_date' : str(out)}
    print(args)
    # return render(request, 'index.html', {'total_consumption_by_date' : out, 'avg_block' : c})
    #****** requesting the tds value from thingspeak server ****
    response = requests.get('http://api.thingspeak.com/channels/1013047/fields/1/last.json?api_key=D7RYNL5OMNRC5RMJ&status=true')
    tds_data = response.json()
    tds = round(float(tds_data['field1']), 2)
    print("Printing tds value")
    print(tds)
    return render(request, 'index.html', {'total_consumption_by_date' : out, 'avg_block' : c, 'nrw' : nrw, 'leakages' : leak, 'tds' : tds })

def avg_consumption_2(request):
    return render(request, 'avg_consumption_2.html')

def ranking(request):
    curr_yr = date.today().year - 1
    curr = date.today().replace(year = curr_yr)
    out = Final.get_by_date(Final, curr)
    a, b, c = Final.get_avg_by_block(Final)
    return render(request, 'ranking.html', {'avg_block' : c})

def curr_week_consumption(request):
    return render(request, 'curr_week_consumption.html')

# def login(request):
#     return render(request, 'login.html')

def season_consumption(request):
    return render(request, 'season_consumption.html')

def season_consumption_sunburst(request):
    return render(request, 'season_consumption_sunburst.html')

def weekday_consumption(request):
    return render(request, 'weekday_consumption.html')
