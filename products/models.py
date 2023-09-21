from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    sub_category = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        ordering = ["title"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name="products")
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
