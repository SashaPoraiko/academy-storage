from django.test import TestCase

from storage.models import Storage, Device, Part


class PhoneModelModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        part = Part.objects.create(name='Big', condition=8)
        device = Device.objects.create(part=part)
        cls.storage = Storage.objects.create(locker='locker', row=1, column=1, device=device)

    def test_fields_required_length(self):
        max_length_locker = self.storage._meta.get_field('locker').max_length
        self.assertEquals(max_length_locker, 80)

    def test_valid_row(self):
        row = self.storage.row
        self.assertTrue(0 < row <= 10)

    def test_valid_column(self):
        column = self.storage.column
        self.assertTrue(0 < column <= 10)
