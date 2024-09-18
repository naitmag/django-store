from django.db import models
from django.utils.translation import gettext_lazy as _

from goods.models import Products
from users.models import User


class OrderitemQuetySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name=_('User'),
                             default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('Order creation date'))
    phone_number = models.CharField(max_length=20, verbose_name=_('Phone number'))
    requires_delivery = models.BooleanField(default=False, verbose_name=_('Delivery required'))
    delivery_address = models.TextField(null=True, blank=True, verbose_name=_('Delivery address'))
    payment_on_get = models.BooleanField(default=False, verbose_name=_('Payment on receipt'))
    is_paid = models.BooleanField(default=False, verbose_name=_('Paid'))
    status = models.CharField(max_length=50, default=_('In processing'), verbose_name=_('Order status'))

    class Meta:
        db_table = 'order'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return _("Order № {order} | Customer {customer_name} {customer_last_name}").format(
            order=self.pk,
            customer_name=self.user.first_name,
            customer_last_name=self.user.last_name
        )


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name=_('Order'))
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, blank=True,
                                verbose_name=_('Product'), default=None)
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name=_('Price'))
    quantity = models.PositiveIntegerField(default=0, verbose_name=_('Quantity'))
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of sale'))

    class Meta:
        db_table = 'order_item'
        verbose_name = _("Order item")
        verbose_name_plural = _("Order items")

    objects = OrderitemQuetySet.as_manager()

    def product_price(self):
        return round(self.price * self.quantity, 2)

    def __str__(self):
        return _('Item {name} | Order № {order}').format(
            name=self.name,
            order=self.order.pk
        )
