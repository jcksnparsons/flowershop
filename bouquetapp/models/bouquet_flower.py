from django.db import models


class BouquetFlower(models.Model):

    flower = models.ForeignKey("Flower", on_delete=models.CASCADE)
    bouquet = models.ForeignKey("Bouquet", on_delete=models.CASCADE)
    quantity = models.IntegerField()
