from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import fundamentalanalysis as fa
from yahoo_fin.stock_info import *
from yahoo_fin import news
from .financials import cashFlow, balanceSheet, incomeStatement #.financials means import from current package
# Create your views here.


def home(request):
    return render(request, 'home.html')


def getInfo(request, ticker):
    apiKey = "bdb926020e885632b760c8a5f35b7e8b"
    """ print(fa.quote("ACB", apiKey)) """
    """ print(fa.balance_sheet_statement("ACB", apiKey, period="quarter")) """

   
    balanceSheetData = balanceSheet()
    incomeStatementData = incomeStatement()
    cashFlowData = cashFlow()
    newsArticles = getNews()
   
    
    print(cashFlowData)


    """ GET POST INFO ON GOOGLE FIANANCE
     if request.method == "POST":
        tickerSearched = request.POST.get("searched","") #second one is default
        exchange = request.POST.get("exchanges", "")
      
    """
    return render(request, "search.html",{
        'ticker':tickerSearched,
    })

def getNews():
    newsArticles = []
    for value in news.get_yf_rss("nflx"):
        tempArray = []
        tempArray.append(value.get('summary'))
        tempArray.append(value.get('link'))
        newsArticles.append(tempArray)


    return newsArticles

