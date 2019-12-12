from rest_framework.test import APITestCase

from storage.api.storage.serializers import StorageReadSerializer, StorageWriteSerializer, StorageFilterSerializer
from storage.models import Part, Device, Storage


class StorageSerializerTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        prt = {
            'name': 'Big',
            'condition': 8,
        }
        part = Part.objects.create(**prt)
        dvc = {
            'part': prt,
        }
        device = Device.objects.create(part=part)

        cls.data = {
            "locker": "the_locker X",
            "row": 1,
            "column": 1,
            "device": device
        }
        cls.invalid_data = {
            "device": device
        }
        cls.read_data = cls.data.copy()
        cls.read_data.update({
            'device': dvc
        })

    def test_read(self):

        serializer = StorageReadSerializer(instance=Storage.objects.create(**self.data))
        self.assertIn("id", serializer.data)
        self.assertEqual(serializer.data['id'], 1)

        for key, value in self.read_data.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, serializer.data)
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        with self.subTest(key=key, sub_key=sub_key, sub_value=sub_value):
                            self.assertIn(sub_key, serializer.data[key])
                            self.assertEqual(serializer.data[key][sub_key], sub_value)
                else:
                    self.assertEqual(serializer.data[key], value)

    # def test_valid_write(self):
    #     serializer = StorageWriteSerializer(data=self.data)
    #     self.assertTrue(serializer.is_valid())

    def test_valid_filter(self):
        serializer = StorageFilterSerializer()
        apply_filters = serializer.validate(self.data)
        self.assertTrue(apply_filters)

    def test_invalid_filter(self):
        serializer = StorageFilterSerializer()
        apply_filters = serializer.validate(self.invalid_data)
        self.assertFalse(apply_filters)
