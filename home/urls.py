from django.urls import path
from home.views import index, createNewStockMonitor


urlpatterns = [
    path('',index, name='index'),
    path('createNewStockMonitor/',createNewStockMonitor,name='createNewStockMonitor')
]