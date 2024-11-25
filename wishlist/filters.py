from django_filters import rest_framework as filters
from .models import Wishlist, Product

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    category = filters.CharFilter(lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['name', 'category', 'min_price', 'max_price']

class WishlistFilter(filters.FilterSet):
    product_name = filters.CharFilter(field_name="product__name", lookup_expr='icontains')
    category = filters.CharFilter(field_name="product__category", lookup_expr='icontains')

    class Meta:
        model = Wishlist
        fields = ['product_name', 'category']
