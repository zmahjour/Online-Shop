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


