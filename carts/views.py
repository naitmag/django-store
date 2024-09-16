from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View

from carts.mixins import CartMixin
from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products


# TODO strings config
class CartAddView(CartMixin, View):
    def post(self, request):
        product_id = request.POST.get("product_id")

        product = Products.objects.get(id=product_id)

        cart = self.get_cart(request, product=product)

        if cart:
            cart.quantity += 1
            cart.save()
        else:
            is_authenticated = request.user.is_authenticated
            Cart.objects.create(user=request.user if is_authenticated else None,
                                session_key=request.session.session_key if not is_authenticated else None,
                                product=product, quantity=1)

        response_data = {
            'message': "Товар добавлен в корзину",
            'cart_items_html': self.render_cart(request)
        }

        return JsonResponse(response_data)


# TODO strings config
class CartChangeView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")

        cart = self.get_cart(request, cart_id=cart_id)

        cart.quantity = request.POST.quantity
        cart.save()

        quantity = cart.quantity

        response_data = {
            'message': "Колличество изменено",
            'quantity': quantity,
            'cart_items_html': self.render_cart(request)
        }

        return JsonResponse(response_data)


# TODO strings config
class CartRemoveView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")

        cart = self.get_cart(request, cart_id=cart_id)
        quantity = cart.quantity
        cart.delete()

        response_data = {
            'message': "Товар удален из корзины",
            'quantity': quantity,
            'cart_items_html': self.render_cart(request)
        }

        return JsonResponse(response_data)
