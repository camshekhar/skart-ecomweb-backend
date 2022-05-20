from django.contrib import admin
from .models import Product, Category, SubCategory, Cart, OrderSummary

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    
admin.site.register(Category, CategoryAdmin)     
    
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')    
   
admin.site.register(SubCategory, SubCategoryAdmin) 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color', 'size', 'desc')
   
admin.site.register(Product, ProductAdmin) 

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'color', 'size', 'price', 'quantity')
   
admin.site.register(Cart, CartAdmin) 

class OrderSummaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'subTotal', 'shippingCharge', 'discount', 'total')
   
admin.site.register(OrderSummary, OrderSummaryAdmin) 

