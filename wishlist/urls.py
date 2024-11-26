from django.urls import path
from .views import ProductListView, WishlistListCreateView, WishlistDeleteView

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('wishlist/', WishlistListCreateView.as_view(), name='wishlist-list-create'),
    path('wishlist/<int:pk>/', WishlistDeleteView.as_view(), name='wishlist-delete'),
]
