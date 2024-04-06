#Forms are basically used for taking input from the user in some manner and 
#using that information for logical operations on database

from django.forms import ModelForm
from django import forms
from .models import MyModel
from django.contrib.auth.models import User 




class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["Item_name", "Quant_ity",]
    labels = {'Item_name': "Item Name", "Quant_ity": "Quantity",}