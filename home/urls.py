from django.urls import path
from home.views import index, createNewStockMonitor,deleteStockMonitor,getAllStockFromUser,updateStockInfo


urlpatterns = [
    path('',index, name='index'),
    path('createNewStockMonitor/',createNewStockMonitor,name='createNewStockMonitor'),
    path('deleteStockMonitor/<int:stock_id>/',deleteStockMonitor,name='deleteStockMonitor'),
    path('getAllStockFromUser/',getAllStockFromUser,name='getAllStockFromUser'),
    path('updateStockInfo/<int:stock_id>',updateStockInfo,name='updateStockInfo'),
]