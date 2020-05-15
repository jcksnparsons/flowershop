from django.db import models
from django.urls import reverse


class Flower(models.Model):

    name = models.CharField(max_length=100)
    binomial_name = models.CharField(max_length=100)
    longevity_in_days = models.IntegerField()
    bouquets = models.ManyToManyField("Bouquet", through='BouquetFlower')

    class Meta:
        verbose_name = ("Flower")
        verbose_name_plural = ("Flowers")

    def __str__(self):
        return f"{self.name} ({self.binomial_name})"

    def get_absolute_url(self):
        return reverse("Flower_detail", kwargs={"pk": self.pk})
