from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import StockMonitor
from home.utils.stock_functions import getStockInfo,verifyStockInfo
from home.forms import StockForms

def index (request):
    stockInfo = []
    #Get stock's name associated with the current user
    if(request.user.is_authenticated):
        stockObjects = StockMonitor.objects.filter(userId = request.user.id)
        if(stockObjects.__len__ != 0):
            for element in stockObjects:
                stock = getStockInfo(element.name,element.updateTime)
                #Se minha api estiver com o limite diario atinginfo, nao irei passar informacoes para meu array e irei passar
                # minha mensagem padrao de erro
                if 'error' in stock:
                    #Adicionar apenas uma vez a mensagem de erro no array
                    if len(stockInfo) == 0:
                        stockInfo.append(stock)
                    break

                stock["id"] = element.id
                stock["typeOfLimit"] = element.typeOfLimit
                stock["upperLimitStatic"] = element.upperLimitStatic
                stock["lowerLimitStatic"] = element.lowerLimitStatic
                stock["upperLimitDinamic"] = element.upperLimitDinamic
                stock["lowerLimitDinamic"] = element.lowerLimitDinamic
                stock["basePrice"] = element.basePrice
                
                stockInfo.append(stock)
                   
    return render(request,'home/index.html',{'stockInfo':stockInfo})

def createNewStockMonitor (request):
    form = StockForms(initial={'userId':request.user})
    if request.method == 'POST':
        form = StockForms(request.POST)
        if form.is_valid():
            form.save(commit=False)
            
            #Verificar se é válido o símbolo da ação que o usuário colocou
            requestInfo = verifyStockInfo(form["name"].value())
            if "Error Message" in requestInfo:
                messages.error(request,requestInfo["Error Message"])
                return redirect ('createNewStockMonitor')
            #Limite de api diário atingido
            elif "error" in requestInfo:
                messages.error(request,'Limite de api diário atingido.')
                return redirect ('createNewStockMonitor')

            form.save()
            messages.success(request,'Nova ação cadastrada com sucesso!')
            return redirect('index')
        else:
            print(form.errors)

    return render(request,'home/createNewStockMonitor.html',{'form':form})

def deleteStockMonitor (request,stock_id):
    stockToBeDeleted = StockMonitor.objects.get(id=stock_id)
    stockToBeDeleted.delete()
    messages.success(request,'Deleção feita com sucesso!')
    return redirect('index')