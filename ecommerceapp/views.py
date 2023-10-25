from django.shortcuts import render, get_object_or_404
from . models import Product
from cart.forms import CartAddProductForm






# Create your views here.
def index(request):
    products = Product.objects.all() #get all products
    context = {
        'products': products
    }
    
    return render(request, 'ecommerceapp/index.html', context)

def product_list(request):

    products = Product.objects.all() #get all products
    context = {
        'products': products
    }

    return render(request, 'ecommerceapp/products.html', context)

def product_detail(request, id):

    product = get_object_or_404(Product, pk=id) # get single data
    cart_product_form = CartAddProductForm()
    context = {
    'product' : product,
    'cart_product_form' : cart_product_form,
    }

    return render(request, 'ecommerceapp/single-product.html', context)

