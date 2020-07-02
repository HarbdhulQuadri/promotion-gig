from django.db import models
from django.urls import reverse # new
import uuid
# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=300)
    description = models.TextField() 
    photo = models.ImageField(upload_to='static/product_photo',blank=True)
    basic_price = models.DecimalField(max_digits=6, decimal_places=2)
    standard_price = models.DecimalField(max_digits=6, decimal_places=2)
    premium_price = models.DecimalField(max_digits=6, decimal_places=2)

'''class CustomerInfo(models.Model):
    full_name= models.CharField(max_length  = 150)
    email= models.EmailField()
    phone_number = models.CharField(max_length= 20)
    address = models.CharField(max_length = 150)
    Tracklink =models.URLField(max_length=128,db_index=True,unique=True, blank=True)
    keyword = models.CharField(max_length = 150)
    came_across= models.CharField(max_length = 150)
'''



