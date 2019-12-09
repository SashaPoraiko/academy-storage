from django.test import TestCase

from storage.models import Part


class PartModelModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.part = Part.objects.create(name='Big', condition=8)

    def test_fields_max_length(self):
        max_length_name = self.part._meta.get_field('name').max_length
        self.assertEquals(max_length_name, 80)

    def test_condition(self):
        cond = self.part.condition
        self.assertTrue(0 < cond <= 10)
