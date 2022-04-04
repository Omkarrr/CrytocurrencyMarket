import json.encoder
import time

import pandas
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import CDN
from pycoingecko import CoinGeckoAPI
from django.contrib.sites import requests
from django.shortcuts import render
import json as JSON
from requests import get as reget

def home(request):
    return render(request,'home.html')


def index(request):
    lala = (int(time.time()) - 60 * 10)
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = reget(url)
    data = data.json()


    return render(request, 'index.html', {"data": data, "lala": lala})

