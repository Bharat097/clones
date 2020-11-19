from django.db import models
from user_service.models import User
from store.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)

    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    time_added = models.DateTimeField(auto_now_add=True)
