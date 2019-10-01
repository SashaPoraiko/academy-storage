from django.db import models
from django.utils import timezone


class Phone(models.Model):
    phone_model = models.ForeignKey('storage.PhoneModel', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    date_release = models.DateTimeField(default=timezone.now)
    date_create = models.DateTimeField(default=timezone.now)
    date_modify = models.DateTimeField(default=timezone.now)
