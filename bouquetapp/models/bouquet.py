from django.db import models
from django.urls import reverse


class Bouquet(models.Model):

    name = models.CharField(max_length=100)
    occasion = models.CharField(max_length=100)
    flowers = models.ManyToManyField("Flower", through='BouquetFlower')

    class Meta:
        verbose_name = ("Bouquet")
        verbose_name_plural = ("Bouquets")

    def __str__(self):
        return f"{self.name} ({self.occasion})"

    def get_absolute_url(self):
        return reverse("Bouquet_detail", kwargs={"pk": self.pk})
