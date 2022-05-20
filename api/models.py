
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length= 100, primary_key = True)
    desc = models.CharField(max_length= 200)
    image = models.CharField(max_length= 300)
    
    def __str__(self):
        return self.title
    
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length= 100, primary_key = True)
    desc = models.CharField(max_length= 200)
    image = models.CharField(max_length= 300)  
    
    def __str__(self):
        return self.title
      
    
class Product(models.Model):
    id = models.CharField(max_length= 100, primary_key = True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, default="ffsf")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default="dfd")
    title = models.CharField(max_length= 100)
    desc = models.CharField(max_length= 200)
    color = models.CharField(max_length= 100)
    size = models.CharField(max_length= 100)
    image  = models.CharField(max_length= 300)
    price = models.CharField(max_length= 100, default="0")
    stockCount = models.IntegerField(default="0")
    
    def __str__(self):
        return self.title
    
class Cart(models.Model):
    id = models.CharField(max_length= 100, primary_key = True)
    title = models.CharField(max_length= 100)
    color = models.CharField(max_length= 100)
    size = models.CharField(max_length= 20)
    image  = models.CharField(max_length= 300)
    quantity = models.CharField(max_length= 20)
    price = models.CharField(max_length= 100, default="0")
   
class OrderSummary(models.Model):
    id = models.OneToOneField(Cart, models.CASCADE , primary_key= True)                  
    subTotal = models.CharField(max_length= 100)
    discount = models.CharField(max_length= 100)
    shippingCharge = models.CharField(max_length= 100, default="100")
    total = models.CharField(max_length=100)   

    
