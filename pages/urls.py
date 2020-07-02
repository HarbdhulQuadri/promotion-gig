from django.urls import path,include
from . import views
from .views import HomePageView, AboutPageView, ContactPageView, ServicesPageView,ProductPageView,OrdersPageView
urlpatterns = [
    path('',HomePageView.as_view(),  name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('service/', ServicesPageView.as_view(), name='service'),
    path('<int:pk>', ProductPageView.as_view(), name='pricing'),
  


    #path('<int:pk>', ProductPageView.as_view(), name='pricing'),
    #path('customer_info', views.customer_info,name='customer_info')
]
#

