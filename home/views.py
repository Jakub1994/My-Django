from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def index(request):
    """A view to return the index page"""

    return render(request, 'home/index.html')


def all_products(request):
    """A view to return the index page"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'home/index.html', context)
