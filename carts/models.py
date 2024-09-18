from django.db import models
from django.utils.translation import gettext_lazy as _

from goods.models import Products
from users.models import User


class CartQuerrySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)

        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('User'))
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name=_('Product'))
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name=_('Quantity'))
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('Date added'))

    class Meta:
        db_table = 'cart'
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    objects = CartQuerrySet().as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return _("Cart {user} | Product {product} | Quantity {quantity}").format(
                user=self.user.username,
                product=self.product.name,
                quantity=self.quantity
            )

        return _("Anonymous cart | Product {product} | Quantity {quantity}").format(
            product=self.product.name,
            quantity=self.quantity
        )
