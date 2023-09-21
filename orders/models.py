from django.db import models
from accounts.models import User
from products.models import Product


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "Pending"
        PROCESSING = "Processing"
        SENDING = "Sending"
        CANCELLED = "Cancelled"
        DELIVERED = "Delivered"

    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="orders"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choices)
    is_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["is_paid", "-updated"]

    def __str__(self):
        return f"order: {self.id} | status: {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.id}"
