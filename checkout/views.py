from django.shortcuts import render, redirect
from .forms import CheckoutForm
from django.views.generic import View
# Create your views here.


def checkout(request):
    """A view to return the index page"""

    return render(request, 'checkout/checkout.html')