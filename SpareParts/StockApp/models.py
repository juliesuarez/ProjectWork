#Accessing a user model for registration of the user in django
from django.contrib.auth.models import AbstractUser 

#inheriting from django models to create our custom models(tables)
from django.db import models

#enables you in terms of time and date
from django.utils import timezone

#enables you avoid negative integers in your columns.
from django.core.validators import MinValueValidator

# Create your models here.





#here we are inheriting from the models.Model in django to create our custom model(table)
class Category(models.Model):# created a table called category
    name = models.CharField(max_length=50,null=False,blank=False,unique=True)

    def __str__(self): #describes how this class category will be referred to as its name.
        return self.name 
    
#creating a model for product
class SparePart(models.Model):
    #creating a relationship between Product and Category.
    Category_name = models.ForeignKey(Category,on_delete=models.CASCADE,null=False,blank=False)
    date_of_arrival = models.DateField(default=timezone.now)
    part_name = models.CharField(max_length=50,null=False,blank=False)
    country_of_origin = models.CharField(max_length=50,null=False,blank=False)
    total_quantity = models.IntegerField(default=0,null=False,blank=False,validators=[MinValueValidator(1)])
    issued_quantity = models.IntegerField(default=0,null=False,blank=False)
    received_quantity = models.IntegerField(default=0,null=False,blank=False)
    unit_price = models.IntegerField(default=0,null=False,blank=False)
    branch_name = models.CharField(max_length=50,null=False,blank=False)

    #this method/function enables you to access properties of the class created below.
    def __str__(self):
        return self.part_name
    


#items in parethesis enable us to validate our fields.
class Sale(models.Model):
    #creating a relationship between class Product and Sale.
    part = models.ForeignKey(SparePart,on_delete=models.CASCADE,null=False,blank=False)
    quantity = models.IntegerField(default=0,null=False,blank=False)
    amount_received = models.IntegerField(default=0,null=False,blank=False)
    customer_name = models.CharField(max_length=100,null=False,blank=False)
    unit_price = models.IntegerField(default=0,null=False,blank=False)
    branch_name = models.CharField(max_length=50,null=False,blank=False)
    phone_number = models.CharField(max_length=50,null=False,blank=False)
    part_name = models.CharField(max_length=50,null=False,blank=False)
    date = models.DateField(default=timezone.now)



    #here we are getting the total amount got after selling a given quantity of stock at a given unit price.
    def get_total(self):
        total = self.quantity * self.part.unit_price
        return int(total)
    
    #here we are getting the amount the customer is being demanded after paying in installment.
    def amount_due(self):
        amount_due = self.get_total() - self.amount_received
        return abs(int(amount_due))
    
    def __str__(self):
        return self.part.part_name 
    