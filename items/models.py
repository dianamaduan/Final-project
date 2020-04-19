from django.db import models
from django.contrib.auth.models import User
from myauth.models import Company,Foundation,Section,Cards,Users
import time
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name

def upload_product(instance, filename):
    lastDot = filename.rfind('.')
    extension= filename[lastDot:len(filename):1]
    return 'images/products/%s-%s%s' % (instance.title, time.time(), extension)


class Product(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.IntegerField()
    discountprice = models.IntegerField()
    discountPercent = models.IntegerField()
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to=upload_product,blank=True,null=True)
    onsale = models.BooleanField()
    is_active = models.BooleanField(default=True)
    link = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    author = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    
class Comments(models.Model):
    text = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.text

class Rating(models.Model):
    rate = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.rate

class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(default=1)

class Order(models.Model):
    orderDate = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(default=1)
