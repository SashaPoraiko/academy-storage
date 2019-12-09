from rest_framework.test import APITestCase

from storage.api.phone_model.serializers import PhoneModelSerializer
from storage.api.storage.serializers import StorageShortSerializer, StorageReadSerializer, StorageWriteSerializer
from storage.models import PhoneModel, Part, Device, Storage


class StorageSerializerTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        part = Part.objects.create(name='Big', condition=8)
        device = Device.objects.create(part=part)
        cls.data = {
            "locker": "the_locker X",
            "row": 1,
            "column": 1,
            "device": device
        }

    def test_read(self):
        serializer = StorageReadSerializer(instance=Storage.objects.create(**self.data))
        self.assertIn("id", serializer.data)
        self.assertEqual(serializer.data['id'], 1)
        print(serializer.data)
        # for key, value in self.data.items():
        #     with self.subTest(key=key, value=value):
        #         self.assertIn(key, serializer.data)
        #         self.assertEqual(serializer.data[key], value)

    # def test_valid_write(self):
    #     serializer = StorageWriteSerializer(data=self.data)
    #     self.assertTrue(serializer.is_valid())
