from rest_framework.test import APITestCase

from storage.api.part.serializers import PartWriteSerializer, PartReadSerializer
from storage.models import Part


class PartSerializerTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        phone_models = ({'name': 'asd', 'brand': 'thebrand', 'model_year': 1993},
                        {'name': 'asd', 'brand': 'thebrand', 'model_year': 1993})
        cls.data = {
            "name": "CHIP",
            "condition": 8,
        }
        cls.write_data = {
            "name": "CHIP",
            "condition": 8,
            "phone_models": phone_models
        }

    def test_read(self):
        serializer = PartReadSerializer(instance=Part.objects.create(**self.data))
        self.assertIn("id", serializer.data)
        self.assertEqual(serializer.data['id'], 1)
        for key, value in self.data.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, serializer.data)
                self.assertEqual(serializer.data[key], value)

    # def test_valid_write(self):
    #     serializer = PartWriteSerializer(data=self.write_data)
    #
    #     self.assertTrue(serializer.is_valid())
