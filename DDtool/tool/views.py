from django.shortcuts import render
from bs4 import BeautifulSoup
from numpy import searchsorted
import requests


# Create your views here.
def home(request):
    return render(request, 'home.html')


def getInfo(request, ticker):
    if request.method == "POST":
        tickerSearched = request.POST.get("searched","") #second one is default
        print(tickerSearched)
        return render(request, "search.html",{
            'ticker':tickerSearched,
        })