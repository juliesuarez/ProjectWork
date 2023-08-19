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
#querring (telling the database to get all the products using 'id(unique identifier) can be name,')
    products = SparePart.objects.all().order_by('-id')
#handles the search among the products created above.
    product_filters = ProductFilter(request.GET,queryset = products)
    products = product_filters.qs 
    #returning searched data.
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


#handles user creating
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request,'ProjectWork/register.html',{'form':form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # username must be in lower case
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
            return render(request,'ProjectWork/register.html',{'form':form})

def service(request):
    return render(request,'ProjectWork/service.html')




@login_required #provided by python(django),ensures that you must have loged in
#the method issue_item takes on two parameters ie request(incoming HTTP request) 
# and pk(primary key of the product to be issued.)
#handles issuing of an item for sale.
# it fetches the product for sale using a primary key(pk) issues it using a SaleForm
#after sale successfully it redirects to the receipt view.
def issue_item(request,pk):
    #it retrieves the product to be issued using the Product model & the provided primary key.
    issued_item = SparePart.objects.get(id=pk)
    #an instance of SaleForm is created using the data from (request.POST)
    sales_form =SaleForm(request.POST)

    #here we are checking if the incoming HTTP request is POST.
    if request.method == 'POST':
        #here we are checking if the submitted sales_form is valid.
        if sales_form.is_valid():
            new_sale = sales_form.save(commit=False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            #keeping truck of the stock remaining after sale.
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()

            print(issued_item.part_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)
            #path after action of selling
            return redirect('receipt')
    return render(request,'ProjectWork/issue_item.html',{'sales_form':sales_form})


#access after login
#handles the process of adding items to the stock.
#it fetches the product using its primary key(pk) and then uses AddForm to update the stock of the product.
#after updating the stock it redirects to the home view.
@login_required
def add_to_stock(request,pk):
    issued_item = SparePart.objects.get(id=pk)
    form = AddForm(request.POST)

    #method not post execute line 119
    if request.method == 'POST':
        if form.is_valid():
            added_quantity = int(request.POST['received_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()
            #to add to the remaining stock quantity is reduced.
            print(added_quantity)
            print(issued_item.total_quantity)
            return redirect('home')
    return render(request,'ProjectWork/add_to_stock.html',{'form':form})



#access after login
#fetches a specific product from database using product_id parameter
#provides a template product_detail.html showing the selected product.
@login_required
def product_detail(request,product_id):
    #queries product by id.
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