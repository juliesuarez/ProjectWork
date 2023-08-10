#handling forms for user's display
from django.forms import ModelForm

#here we are importing all models
from .models import *
#from StockApp.models import * 3&4-

#here we importing user's model in django to create our custom user
from django.contrib.auth.models import User

#here we are importing a library in django for creating our user form
from django.contrib.auth.forms import UserCreationForm


#handles a form that the user will use to add the stock
class AddForm(ModelForm): #workers edit here,add received stock.
    class Meta:
        model = Product
        fields = [
            'received_quantity'
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
            'part_name',
            'part_number',
        ]

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]