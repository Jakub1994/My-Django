from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('', views.all_products, name='home'),
    path('', views.product_detail, name='home'),

]
