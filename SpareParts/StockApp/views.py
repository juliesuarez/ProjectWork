from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

#here we import reverse function
from django.urls import reverse

#here import decorators from django
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
    products = Product.objects.all().order_by('-id')
#handles the search among the products created above.
    product_filters = ProductFilter(request.GET,queryset = products)
    products = product_filters.qs 
    #not_negative = products.total_quantity
    #if not_negative <= 0:
     #   products.total_quantity == 0
    #telling django to consider a template home for queries from database.
    return render(request,'ProjectWork/home.html',{'products': products, 'product_filters':product_filters})

def index(request):
    return render(request,'ProjectWork/index.html')

@login_required
def delete_product(request,product_id):
    delete_product = Product.objects.get(id=product_id)
    delete_product.delete()
    return HttpResponseRedirect(reverse('home'))
    
   
@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request,'ProjectWork/receipt.html',{'sales':sales})


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
def issue_item(request,pk):
    #it retrieves the product to be issued using the Product model & the provided primary key.
    issued_item = Product.objects.get(id=pk)
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

            print(issued_item.item_name)
            print(request.POST['quantity'])
            print(issued_item.total_quantity)
            #path after action of selling
            return redirect('receipt')
    return render(request,'ProjectWork/issue_item.html',{'sales_form':sales_form})

@login_required
def add_to_stock(request,pk):
    issued_item = Product.objects.get(id=pk)
    form = AddForm(request.POST)
    
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


@login_required
def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    return render(request,'ProjectWork/product_detail.html',{'product':product})
    


@login_required
def receipt_detail(request,receipt_id):
    receipt = Sale.objects.get(id=receipt_id)
    return render( request,'ProjectWork/receipt_detail.html',{'receipt':receipt})


@login_required
def all_sales(request):
    sales = Sale.objects.all()
    total = sum(items.amount_received for items in sales)
    change = sum(items.get_change() for items in sales)
    net = total-change
    return render(request,'ProjectWork/all_sales.html',{'sales':sales,'total':total,'change': change,'net':net})
  