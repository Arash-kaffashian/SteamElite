from products.models import Product


class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new, no session key! create on!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product):
        product_id = str(product.product_id)

        # logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price_global)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def total_price(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(product_id__in=products_ids)

        total = 0
        for product in products:
            Product.update_prices(product)
            total = total + product.price_global
        return total

    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # Use ids to look up the products in db models
        products = Product.objects.filter(product_id__in = product_ids)
        # Return looked up products
        return products

    def delete(self, product):
        product_id = str(product)
        # Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

