from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .cart import Cart
from products.models import Product


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request, "cart_summary.html", {"cart_products": cart_products})


def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))

        # lookup product in db
        product = get_object_or_404(Product, product_id=product_id)

        # save to session
        cart.add(product=product)

        # Get cart quantity
        cart_quantity = cart.__len__()

        # return response
        response = JsonResponse({'quantity': cart_quantity})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    pass
