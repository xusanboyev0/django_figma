from unicodedata import category

from django.contrib import admin

from .models import Product, Wishlist

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    pass


class WishlistAdmin(admin.ModelAdmin):
    pass


