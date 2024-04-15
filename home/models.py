from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class StockMonitor(models.Model):
    TYPE_OF_LIMIT_CHOICES = [
        ('static','Estático'),
        ('dinamic','Dinâmico')
    ]

    BASE_PRICE_CHOICES=[
        ('ltp','Last Traded Price (LTP)'),
        ('c_last','C-LAST'),
        ('most_recent','Most Recent')
    ]

    UPDATE_TIME_CHOICES=[
         ('1min','1min'),
         ('5min','5min'),
         ('15min','15min'),
         ('30min','30min'),
         ('60min','60min')
    ]

    name = models.CharField(max_length=50,null=False,blank=False)
    completeName = models.CharField(max_length=100,null=False,blank=False)
    updateTime = models.CharField(max_length=100, choices=UPDATE_TIME_CHOICES, null=False,blank=False)
    typeOfLimit = models.CharField(max_length=30, choices=TYPE_OF_LIMIT_CHOICES, null=False,blank=False) 
    upperLimitStatic = models.FloatField(null=True,blank=True)
    lowerLimitStatic = models.FloatField(null=True,blank=True)
    basePrice = models.CharField(max_length=30, choices= BASE_PRICE_CHOICES,null=True,blank=True)
    upperLimitDinamic = models.FloatField(null=True,blank=True)
    lowerLimitDinamic = models.FloatField(null=True,blank=True)
    userId =  models.ForeignKey(
        to=User,
        on_delete = models.SET_NULL,
        null = True,
        blank = False,
        related_name= "user",
    )