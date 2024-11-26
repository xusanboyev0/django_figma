from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Wishlist, Product
from .serializers import WishlistSerializer, ProductSerializer
from .filters import WishlistFilter, ProductFilter


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class WishlistListCreateView(ListCreateAPIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = WishlistFilter

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user).select_related('product')

    def post(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        product = Product.objects.get(id=product_id)
        wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
        if not created:
            return Response({"message": "Mahsulot wishlistda mavjud"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(wishlist_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WishlistDeleteView(DestroyAPIView):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)
