from django.db import models


class ActivityData(models.Model):
    CATEGORY_CHOICES = [
        ('diesel', 'Diesel'),
        ('electricity', 'Electricity'),
        ('explosives', 'Explosives'),
        ('transport', 'Transport'),
    ]

    mine = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)
    date = models.DateField()

    def __str__(self):
        return f"{self.mine} - {self.category} - {self.quantity}"


class EmissionFactor(models.Model):
    source = models.CharField(max_length=50)
    co2_per_unit = models.FloatField()
    unit = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.source} ({self.unit})"



