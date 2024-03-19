from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register((Contact,Checkout,Checkoutproduct,Maincategory,Subcategory,Brand,Buyer,Product,wishlist))

