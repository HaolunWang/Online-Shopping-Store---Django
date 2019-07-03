from django.contrib import admin
from .models import Product, Category, Client, Order
from django.db.models import F
# Register your models here.
#admin.site.register(Product)
admin.site.register(Category)
#admin.site.register(Client)
admin.site.register(Order)


def add_stock(modeladmin, reuqest, queryset):
    queryset.update(stock=F('stock')+50)
    add_stock.short_description = "Add 50 to stock for selected products"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock')
    actions = [add_stock]


admin.site.register(Product, ProductAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('company', 'city', 'shipping_address', 'province')


admin.site.register(Client, ClientAdmin)