from django.urls import path
from home.views import index, createNewStockMonitor,deleteStockMonitor


urlpatterns = [
    path('',index, name='index'),
    path('createNewStockMonitor/',createNewStockMonitor,name='createNewStockMonitor'),
    path('deleteStockMonitor/<int:stock_id>/',deleteStockMonitor,name='deleteStockMonitor'),
]