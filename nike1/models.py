from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='nikeimg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cat = models.CharField(max_length=100)

class Product1(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='nikeimg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cat = models.CharField(max_length=100)    

class Product2(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='nikeimg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cat = models.CharField(max_length=100)    

