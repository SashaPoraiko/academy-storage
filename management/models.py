from django.db import models


class Feedback(models.Model):
    message = models.CharField(max_length=2048)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return ' '.join((self.name, self.email, self.phone))
