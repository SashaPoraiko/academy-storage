from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class PhoneModel(models.Model):
    brand_choises = [
        ('APPLE', 'Apple'),
        ('SAMSUNG', 'Samsung'),
        ('XIAOMI', 'Xiaomi'),
    ]

    name = models.CharField(max_length=200)
    brand = models.CharField(
        max_length=30,
        choices=brand_choises
    )
    model_year = models.IntegerField(
        validators=[MaxValueValidator(timezone.now().year),
                    MinValueValidator(timezone.now().year - 1000)])

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone_model = models.ForeignKey('storage.PhoneModel', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    date_release = models.DateTimeField(default=timezone.now)
    date_create = models.DateTimeField(default=timezone.now)
    date_modify = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.phone_model) + self.comment