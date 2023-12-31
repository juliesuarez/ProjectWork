#handling forms for user's display
from django.forms import ModelForm

#here we are importing all models
from .models import *
#from StockApp.models import * 3&4-

#here we importing user's model in django to create our custom user
from django.contrib.auth.models import User

#here we are importing a library in django for creating our user form
from django.contrib.auth.forms import UserCreationForm


#handles a form that the user will use to add the stock/update stock.
class AddForm(ModelForm): #workers edit here,add received stock.
    #class Meta enables us to edit our table/model or manipulate
    class Meta:
        model = SparePart
        fields = [
            'received_quantity',
            'branch_name'
        ]


class SaleForm(ModelForm):
    #class Meta enables you to edit your model,makes your class dynamic.
    class Meta:
        model = Sale
        fields = [
            'quantity',
            'amount_received',
            'customer_name',
            'branch_name',
            'phone_number',
            'date',
        ]

