#importing an admin library from django to create admin interface.
from django.contrib import admin
from .models import *
# Register your models here.

#here we are registering our models from models.py
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)