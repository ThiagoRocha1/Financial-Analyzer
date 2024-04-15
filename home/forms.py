from django import forms
from home.models import StockMonitor

class StockForms(forms.ModelForm):
    class Meta:
        model = StockMonitor
        fields = '__all__'

        widgets={
            'name': forms.TextInput(
                attrs={'class':'field-wrapper'},
            ),
            'completeName': forms.TextInput(
                attrs={'class':'field-wrapper'}
            ),
            'updateTime': forms.Select(
                attrs={'class':'field-wrapper'}
            ),
            'typeOfLimit': forms.Select(
                attrs={'class':'field-wrapper'}
            ),
            'upperLimitStatic': forms.NumberInput(
                attrs={'class':'field-wrapper'}
            ),
            'lowerLimitStatic': forms.NumberInput(
                attrs={'class':'field-wrapper'}
            ),
            'basePrice': forms.Select(
                attrs={'class':'field-wrapper'}
            ),
            'upperLimitDinamic': forms.NumberInput(
                attrs={'class':'field-wrapper'}
            ),
            'lowerLimitDinamic': forms.NumberInput(
                attrs={'class':'field-wrapper'}
            ),
            'userId': forms.HiddenInput(
                attrs={'class':'field-wrapper'}
            ),
        }

        labels={
            'name':'Nome',
            'completeName':'Nome da ação completo',
            'updateTime':'Tempo de atualização',
            'typeOfLimit':'Tipo de limite',
            'upperLimitStatic':'Limite superior',
            'lowerLimitStatic':'Limite inferior',
            'basePrice':'Preço Base',
            'upperLimitDinamic':'Limite superior (em %)',
            'lowerLimitDinamic':'Limite inferior (em %)',
            'userId':'userId'
        }