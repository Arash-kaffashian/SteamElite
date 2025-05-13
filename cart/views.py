from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .cart import Cart
from products.models import Product


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    total = cart.total_price()
    return render(request, "cart_summary.html", {"cart_products": cart_products, 'total': total})


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
        messages.success(request, "Product successfully added to your cart!")
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        # Call delete function in cart
        cart.delete(product=product_id)

        response = JsonResponse ({'product':product_id})
        # Return redirect('cart-summary')
        messages.success(request, "Product successfully removed from your cart!")
        return response
