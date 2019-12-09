import datetime

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from storage.api.phone.serializers import PhoneReadSerializer, PhoneWriteSerializer
from storage.models import PhoneModel, Phone
from datetime import datetime


class PhoneSerializerTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        author = User.objects.create_superuser('username', 'theemail123@gmail.com', 'Superpassword123')
        phone_model = {
            "name": "IPhone X",
            "brand": "APPLE",
            "model_year": datetime.now().year
        }
        p_m = PhoneModel.objects.create(**phone_model)

        cls.data = {
            'phone_model': p_m,
            'author': author,
            'comment': 'mycomment',
            'date_release': datetime.now(),
            'date_create': datetime.now(),
            'date_modify': datetime.now()
        }

    def test_read(self):
        serializer = PhoneReadSerializer(instance=Phone.objects.create(**self.data))
        print(serializer.data)
        self.assertIn("id", serializer.data)
        self.assertEqual(serializer.data['id'], 1)

    #     for key, value in self.data.items():
    #         with self.subTest(key=key, value=value):
    #             self.assertIn(key, serializer.data)
    #             self.assertEqual(serializer.data[key], value)
    #
    # def test_valid_write(self):
    #     serializer = PhoneWriteSerializer(data=self.data)
    #     self.assertTrue(serializer.is_valid())
