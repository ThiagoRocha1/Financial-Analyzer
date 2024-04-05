from django.shortcuts import render
from home.utils.stock_functions import getStockInfo
import requests

def index (request):
    stock_info = []
    #stock1 = getStockInfo('IBM','5min')
    #stock2 = getStockInfo('ITUB','5min')

    #stock_info.append(stock1)
    #stock_info.append(stock2)


    return render(request,'home/index.html',{'stock_info':stock_info})