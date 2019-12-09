from django.test import TestCase

from storage.models import PhoneModel


class PhoneModelModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.phone_model = PhoneModel.objects.create(name='Big', brand='Bob', model_year=1997)

    def test_fields_max_length(self):
        max_length_name = self.phone_model._meta.get_field('name').max_length
        max_length_brand = self.phone_model._meta.get_field('brand').max_length
        self.assertEquals(max_length_name, 200)
        self.assertEquals(max_length_brand, 30)
