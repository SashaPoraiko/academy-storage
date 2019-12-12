from rest_framework.test import APITestCase

from storage.api.part.serializers import PartWriteSerializer, PartReadSerializer, PartFilterSerializer
from storage.models import Part, PhoneModel


class PartSerializerTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        phone_models = [
            {'name': 'asd', 'brand': 'thebrand', 'model_year': 1993},
            {'name': 'asd', 'brand': 'thebrand', 'model_year': 1993}
        ]
        cls.phone_model_instances = []
        for phone_model in phone_models:
            cls.phone_model_instances.append(PhoneModel.objects.create(**phone_model))

        cls.data = {
            "name": "CHIP",
            "condition": 8
        }
        cls.invalid_data={
            "condition": 8
        }
        cls.read_data = cls.data.copy()
        cls.read_data["phone_models"] = phone_models

        cls.write_data = cls.data.copy()
        cls.write_data["phone_models"] = list(map(lambda x: getattr(x, 'id', None), cls.phone_model_instances))

    def test_read(self):
        part = Part.objects.create(**self.data)
        part.phone_models.set(self.phone_model_instances)
        serializer = PartReadSerializer(instance=part)
        self.assertIn("id", serializer.data)
        self.assertEqual(serializer.data['id'], 1)
        for key, value in self.data.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, serializer.data)
                self.assertEqual(serializer.data[key], value)

    def test_valid_write(self):
        serializer = PartWriteSerializer(data=self.write_data)
        self.assertTrue(serializer.is_valid())

    def test_valid_filter(self):
        serializer = PartFilterSerializer()
        apply_filters = serializer.validate(self.data)
        self.assertTrue(apply_filters)

    def test_invalid_filter(self):
        serializer = PartFilterSerializer()
        apply_filters = serializer.validate(self.invalid_data)
        self.assertFalse(apply_filters)