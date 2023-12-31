from django.urls import path
#let us reuse the Django login view
from django.contrib.auth import views as auth_views


#lets import our views from the application StockApp
from StockApp import views
urlpatterns = [

    #index page
    path('', views.index, name='index'),

    #home page
    path('home', views.home, name='home'),
    path('home/<int:product_id>', views.product_detail, name='product_detail'),


    #receipt issuing
    path('receipt/', views.receipt, name='receipt'),
    path('receipt_detail/<int:receipt_id>', views.receipt_detail, name='receipt_detail'),

    #sales made
    path('all_sales/', views.all_sales, name='all_sales'),
    path('issue_item/<int:pk>', views.issue_item, name='issue_item'),
   

    #add to stock by user
    path('add_to_stock/<int:pk>', views.add_to_stock, name='add_to_stock'),


    #login & logout
    path('login/', auth_views.LoginView.as_view(template_name = 'ProjectWork/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='ProjectWork/logout.html'),name='logout'),
    
]