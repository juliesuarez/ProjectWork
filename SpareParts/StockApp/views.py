from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

#here we import reverse function
from django.urls import reverse

#here import decorators from django,Used to check authetication of the user.
from django.contrib.auth.decorators import login_required

#here we are importing models
from .models import *

#here importing forms ie AddForm,SaleForm
from .forms import *

#here importing filters ie filters
from .filters import *

# Create your views here.
def home(request):
    #return render(request,'ProjectWork/home.html'),dead code
#querring (telling the database to get all the instances of sparepart using 'id(unique identifier) can be name,')
#'-id' is descending order,which displays the latest item first.
    products = SparePart.objects.all().order_by('-id')
#handles the search among the products created above.
    product_filters = ProductFilter(request.GET,queryset = products)
    #returns searched/filtered data/queryset.
    products = product_filters.qs 
    #telling django to consider a template home for queries from database.
    return render(request,'ProjectWork/home.html',{'products': products, 'product_filters':product_filters})

def index(request):
    return render(request,'ProjectWork/index.html')


#access after login  
#this retrieves a list of sales records from the module Sale
#orders by the id
#renders a template receipt.html for displaying all the receipts.
#the dictionary has a variable sale where all sales are stored that are to be rendered.
@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request,'ProjectWork/receipt.html',{'sales':sales})


@login_required #provided by python(django),ensures that you must have loged in
#the method issue_item takes on two parameters ie request(incoming HTTP request) 
# and pk(primary key of the product to be issued.)
#handles issuing of an item for sale.
# it fetches the product for sale using a primary key(pk) issues it using a SaleForm
#after sale successfully it redirects to the receipt view.

# ...
#retrieves a SparePart object from the database using the given pk (primary key) as the identifier. 
#takes two parameters ie request and primary key
def issue_item(request, pk):
    #The pk is typically used to uniquely identify a record/set of data  in the database.
    issued_item = SparePart.objects.get(id=pk)
    #here whether the form has been submitted.
    if request.method == 'POST':    
        # initializes a SaleForm instance with the data from the request.POST data, 
        # which contains the form data submitted by the user.
        sales_form = SaleForm(request.POST)
        #checks if the submitted data in the form is valid basing form validation rules.
        if sales_form.is_valid():
            #commit=False prevents the instance/object from being saved to database immediately.
            new_sale = sales_form.save(commit=False)
            new_sale.part = issued_item
            new_sale.unit_price = issued_item.unit_price
            #saving to the database.
            new_sale.save()

            # Update the remaining stock quantity
            issued_quantity = new_sale.quantity
            #total quantity of issued item reduced by issued quantity.
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            return redirect('receipt')

    else:
        sales_form = SaleForm()

    return render(request, 'ProjectWork/issue_item.html', {'sales_form': sales_form})



#access after login
#handles the process of adding items to the stock.
#it fetches the product using its primary key(pk) and then uses AddForm to update the stock of the product.
#after updating the stock it redirects to the home view.
@login_required
def add_to_stock(request,pk):
    #gets the sparepart by the primary key.
    issued_item = SparePart.objects.get(id=pk)
    # form prompts the user to input the quantity of items to be added.
    form = AddForm(request.POST)

    #method not post execute line 119
    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            #here the total quantity is increased by the added quantity.
            issued_item.total_quantity += added_quantity
            #issued_item is saved to reflect the added quantity.
            issued_item.save()
            #to add to the remaining stock quantity is reduced.
            print(added_quantity)
            print(issued_item.total_quantity)
            #redirected to home page where the user can see the updated stock.
            return redirect('home')
    return render(request,'ProjectWork/add_to_stock.html',{'form':form})



#access after login
#fetches a specific product from database using product_id parameter
#provides a template product_detail.html showing the selected product.
@login_required
def product_detail(request,product_id):
    #queries product by product_id.
    product = SparePart.objects.get(id=product_id)
    return render(request,'ProjectWork/product_detail.html',{'product':product})
    


#access after login
#fetches the sales receipt from the database using a receipt id parameter
#renders the template receipt_detail.html for displaying the information about the receipt for items purchased.
@login_required
def receipt_detail(request,receipt_id):
    #below is a query
    #querying data by id
    receipt = Sale.objects.get(id=receipt_id)
    return render( request,'ProjectWork/receipt_detail.html',{'receipt':receipt})



#access after login
# this retrieves a list of all sale records from the database
#it calculates total,change and net values using the sales data
#the results are rendered in all_sales.html template.
#the dictionary renders the values stored in the respective variables as required.
@login_required
def all_sales(request):
    #querying all data from the module sale
    sales = Sale.objects.all()
    total = sum(items.amount_received for items in sales)
    amount_due = sum(items.amount_due() for items in sales)
    cash_at_hand = total-amount_due
    total_sales = total + amount_due
    return render(request,'ProjectWork/all_sales.html',{'sales':sales,'total':total,'amount_due': amount_due,'cash_at_hand':cash_at_hand,'total_sales':total_sales})
  
#dictionaries in the fuction enable us send variables to the views