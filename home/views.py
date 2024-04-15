from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import StockMonitor
from home.utils.stock_functions import getStockInfo
from home.forms import StockForms
import requests

def index (request):
    stockInfo = []
    #Get stock's name associated with the current user
    if(request.user.is_authenticated):
        stockObjects = StockMonitor.objects.filter(userId = request.user.id)
        if(stockObjects.__len__ != 0):
            for element in stockObjects:
                stock = getStockInfo(element.name,element.updateTime)
                stockInfo.append(stock)
          
    return render(request,'home/index.html',{'stockInfo':stockInfo})

def createNewStockMonitor (request):
    form = StockForms(initial={'userId':request.user})
    if request.method == 'POST':
        form = StockForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Nova ação cadastrada com sucesso!')
            return redirect('index')
        else:
            print(form.errors)

    return render(request,'home/createNewStockMonitor.html',{'form':form})