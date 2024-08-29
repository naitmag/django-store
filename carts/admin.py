from django.contrib import admin

from carts.models import Cart


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'created_timestamp'
    search_fields = 'product', 'quantity', 'created_timestamp'
    readonly_fields = ('created_timestamp',)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product_display', 'quantity', 'created_timestamp']
    list_filter = ['created_timestamp', 'user', 'product__name']

    @staticmethod
    def user_display(obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"

    @staticmethod
    def product_display(obj):
        return str(obj.product.name)
