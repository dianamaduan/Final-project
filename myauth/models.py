from django.db import models
from django.contrib.auth.models import User
class Users(models.Model):
    name = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200, unique=True)
    cardBalance = models.FloatField(default=0)
    address = models.CharField(max_length=200, unique=True)
    users = models.OneToOneField(User, on_delete=models.CASCADE,unique=False)
    def __str__(self):
        return self.name
        
class Foundation(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200, unique=True)
    cardBalance = models.FloatField()
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Cards(models.Model):
    cardNumber = models.CharField(max_length=12, unique=True)
    cvv = models.IntegerField()
    balance = models.FloatField()
    validDate = models.DateField(auto_now=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.cardNumber

class Company(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True,blank=True, null=True)
    description = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200, unique=True)
    cardBalance = models.FloatField(default=0)
    address = models.CharField(max_length=200, unique=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class Section(models.Model):
    name = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.name

class Destitute(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    iin = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200, unique=True)
    cardNumber = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='',blank=True,null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE,blank=True,null=True)
    