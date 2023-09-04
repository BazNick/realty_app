from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RealEstateOffer(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_start = models.DateField()
    date_end = models.DateField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
