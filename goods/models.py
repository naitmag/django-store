from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name=_('Name'))
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return f"[{self.pk}] {self.name}"


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name=_('Name'))
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name=_('Image'))
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name=_('Price'))
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name=_('Sale'))
    quantity = models.PositiveIntegerField(default=0, verbose_name=_('Quantity'))
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name=_('Category'))

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ("id",)

    def __str__(self):
        return f"[{self.pk}] {self.name} ({self.quantity})"

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={'product_slug': self.slug})

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
