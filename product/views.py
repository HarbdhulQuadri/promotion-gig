from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Product
class ProductListView(ListView):
    model = Product
    template_name = 'product/index1.html'
