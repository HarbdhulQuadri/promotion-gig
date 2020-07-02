from django.shortcuts import render
from django.views.generic import ListView,TemplateView,DetailView  
from product.models import Product
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse

#from product.forms import CustomerInfoForm

# Create your views here.
class HomePageView(ListView):
    template_name = 'index.html'
    def get_queryset(self):

        """Return the products"""
        return Product.objects.all
class AboutPageView(TemplateView):
    template_name = 'about-us.html'
class ContactPageView(TemplateView):
    template_name = 'contact.html'

class ServicesPageView(ListView):
    template_name = 'services.html'
    def get_queryset(self): 
        """Return the products"""
        return Product.objects.all


class ProductPageView(DetailView): # new
    template_name = 'pricing.html'
    
    def get_queryset(self):
        return Product.objects.all()
        #Plan.objects.all()
        #b= Plan.objects.get(plan_name="Basic")
        #s=Plan.objects.get(plan_name="Standard")
        #p= Plan.objects.get(plan_name="Premium")
        #b = b.price
        #s= s.price
        #p= p.price
class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'   
    def get_queryset(self):
        return Product.objects.all()    

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'
    def get_queryset(self):
        return Product.objects.all() 


