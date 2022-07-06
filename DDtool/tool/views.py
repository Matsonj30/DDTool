from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import fundamentalanalysis as fa
from yahoo_fin.stock_info import *
from yahoo_fin import news
# Create your views here.
def home(request):
    return render(request, 'home.html')


def getInfo(request, ticker):
    apiKey = "bdb926020e885632b760c8a5f35b7e8b"
    """ print(fa.quote("ACB", apiKey)) """
    """ print(fa.balance_sheet_statement("ACB", apiKey, period="quarter")) """

   
    balanceSheetData = balanceSheet()
    newsArticles = getNews()
   









    """ GET POST INFO ON GOOGLE FIANANCE
     if request.method == "POST":
        tickerSearched = request.POST.get("searched","") #second one is default
        exchange = request.POST.get("exchanges", "")
      



        website = requests.get("https://www.google.com/finance/quote/" + str(tickerSearched)+":"+str(exchange))
        soupWebsite = BeautifulSoup(website.text, "html.parser")
        findCompanySite = soupWebsite.find_all("a", {"class": "tBHE4e"})
        print(findCompanySite[-1].decode_contents())
 """



    return render(request, "search.html",{
        'ticker':tickerSearched,
    })

def getNews():
    newsArticles = []
    
    for value in news.get_yf_rss("nflx"):
        tempArray = []
        print(value.get('summary'))
        print(value.get("link"))
        tempArray.append(value.get('summary'))
        tempArray.append(value.get('link'))
        newsArticles.append(tempArray)

    for article in newsArticles:
        print(article)
        print("")

def balanceSheet():
    quartAndAnnual = [] #last four quarters if want?

    annualValues = {} #last four years standing
    annualSheet = (get_balance_sheet("xspa"))


    annualValues["times"] = list(annualSheet) #get X axis titles AKA timeframes
    annualValues["cash"] = annualSheet.loc[['cash']].to_numpy().flatten() #flatten just turns our silly 2D array to 1D
    annualValues["totalAssets"] = annualSheet.loc[['totalAssets']].to_numpy().flatten() 
    annualValues["currentAssets"] = annualSheet.loc[['totalCurrentAssets']].to_numpy().flatten()
    #put non current assets here
    annualValues["inventory"] = annualSheet.loc[['inventory']].to_numpy().flatten()
    annualValues["totalLiabilities"] = annualSheet.loc[['totalLiab']].to_numpy().flatten()
    annualValues["currentLiabilities"] = annualSheet.loc[['totalCurrentLiabilities']].to_numpy().flatten()
    #put noncurrent liabilities here
    
    return annualValues
    



   
