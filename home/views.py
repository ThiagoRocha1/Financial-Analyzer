from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import StockMonitor
from home.utils.stock_functions import getStockInfo,verifyStockInfo,sendEmail
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
                stock["name"] = element.name
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

def getAllStockFromUser (request):
    listStock = []
    stocks = StockMonitor.objects.filter(userId = request.user.id)
    for element in stocks:
        stock = {}
        stock["id"] = element.id
        stock["name"] = element.name
        stock["updateTime"] = element.updateTime
        stock["typeOfLimit"] = element.typeOfLimit
        stock["upperLimitStatic"] = element.upperLimitStatic
        stock["lowerLimitStatic"] = element.lowerLimitStatic
        stock["upperLimitDinamic"] = element.upperLimitDinamic
        stock["lowerLimitDinamic"] = element.lowerLimitDinamic
        stock["basePrice"] = element.basePrice
        listStock.append(stock)

    return JsonResponse(list(listStock),safe=False)

def updateStockInfo(request,stock_id):
   if request.method == 'GET':
      stockElement = StockMonitor.objects.get(id=stock_id)
      stockInfo = getStockInfo(stockElement.name,stockElement.updateTime)
      newInfo ={
      "open_price":stockInfo['open_price'],
      "close_price":stockInfo['close_price'],     
      "highest_price":stockInfo['highest_price'],
      "lowest_price":stockInfo['lowest_price'],
      }
      
   if(stockElement.typeOfLimit == "static"):
      if(float(stockInfo["close_price"]) >= stockElement.upperLimitStatic):
         body = f"""
         <h1>Olá investidor!</h1>
         <p>O Limite superior de {stockElement.upperLimitStatic} foi ultrapassado!</p>
         <p>Isso é uma excelente oportunidade de venda!</p>
         """
         sendEmail(body,['mrthiago09@gmail.com'])
         messages.success(request,'Email enviado com sucesso!')
      elif(float(stockInfo["close_price"]) <= stockElement.lowerLimitStatic):
         body = f"""
         <h1>Olá investidor!</h1>
         <p>O Limite inferior de {stockElement.lowerLimitStatic} foi ultrapassado!</p>
         <p>Isso é uma excelente oportunidade de compra!</p>
         """
         sendEmail(body,['mrthiago09@gmail.com'])
         messages.success(request,'Email enviado com sucesso!')
   else:
      averagePrice = (float(stockInfo["highest_price"]) + float(stockInfo["lowest_price"]))/2
      if(float(stockInfo["close_price"]) >= ((stockElement.upperLimitDinamic*averagePrice)/100) + averagePrice):
         body = f"""
         <h1>Olá investidor!</h1>
         <p>O Limite superior de {stockElement.upperLimitDinamic}% foi ultrapassado!</p>
         <p>Isso é uma excelente oportunidade de venda!</p>
         """
         sendEmail(body,['mrthiago09@gmail.com'])
         messages.success(request,'Email enviado com sucesso!')
      elif(float(stockInfo["close_price"]) <= averagePrice - ((stockElement.lowerLimitDinamic*averagePrice)/100)):
         body = f"""
         <h1>Olá investidor!</h1>
         <p>O Limite inferior de {stockElement.lowerLimitDinamic}% foi ultrapassado!</p>
         <p>Isso é uma excelente oportunidade de compra!</p>
         """

         sendEmail(body,['mrthiago09@gmail.com'])
         messages.success(request,'Email enviado com sucesso!')

   return JsonResponse(newInfo,safe=False)