from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name="checkout"),
    path('thanks/', views.thanks, name='thanks'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook')
]
