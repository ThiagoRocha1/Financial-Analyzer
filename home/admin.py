from django.contrib import admin
from home.models import StockMonitor

# Register your models here.
class ShowingStockTypes (admin.ModelAdmin):
    list_display = ("id","name","userId")
    list_display_links = ("id","name")
    search_fields= ("name","userId")

admin.site.register(StockMonitor,ShowingStockTypes)