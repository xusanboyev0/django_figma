from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, DecimalField, ForeignKey, DateTimeField, CASCADE


class Product(Model):
    name = CharField(max_length=255)
    description = TextField()
    price = DecimalField(max_digits=10, decimal_places=2)
    category = CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Wishlist(Model):
    user = ForeignKey(User, CASCADE, related_name="wishlists")
    product = ForeignKey(Product, CASCADE, related_name="wishlisted_by")
    added_on = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')
        # ordering = ['added_at']