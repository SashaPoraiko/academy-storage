from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


class PhoneModel(models.Model):
    brand_choices = [
        ('APPLE', 'Apple'),
        ('SAMSUNG', 'Samsung'),
        ('XIAOMI', 'Xiaomi'),
    ]

    name = models.CharField(max_length=200)
    brand = models.CharField(
        max_length=30,
        choices=brand_choices
    )
    model_year = models.IntegerField(
        validators=[MaxValueValidator(timezone.now().year),
                    MinValueValidator(timezone.now().year - 1000)])

    def __str__(self):
        return self.name


class Phone(models.Model):
    phone_statuses = [
        ('ACTIVE', 'Active'),
        ('DELETED', 'Deleted')
    ]

    phone_model = models.ForeignKey('storage.PhoneModel', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    condition = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=1)
    date_release = models.DateTimeField(default=timezone.now)
    date_create = models.DateTimeField(default=timezone.now)
    date_modify = models.DateTimeField(default=timezone.now)
    status = models.CharField(default=phone_statuses[0], max_length=30, choices=phone_statuses)

    def __str__(self):
        return ' '.join(map(str, (self.phone_model, self.comment)))


class Part(models.Model):
    name = models.CharField(max_length=80)
    condition = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    phone_models = models.ManyToManyField('storage.PhoneModel')

    def __str__(self):
        return f'name: {self.name}, condition: {self.condition}'


class Device(models.Model):
    part = models.OneToOneField('storage.Part', null=True, blank=True, on_delete=models.PROTECT)
    phone = models.OneToOneField('storage.Phone', null=True, blank=True, on_delete=models.PROTECT)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.part and self.phone:
            raise Exception('Cant hold 2 items')
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'Part:{self.part}' if self.part else f'Phone:{self.phone}'


class Storage(models.Model):
    locker = models.CharField(max_length=80)
    row = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    column = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    device = models.ForeignKey('storage.device', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return ' '.join(map(str, (self.locker, self.row, self.column)))
