import datetime

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from storage.api.phone.serializers import PhoneReadSerializer, PhoneWriteSerializer
from storage.models import PhoneModel, Phone
from datetime import datetime


class PhoneSerializerTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        author = {
            'username': 'username',
            'email': 'theemail123@gmail.com',
        }
        author_instance = User.objects.create_user(password='Superpassword123', **author)
        phone_model = {
            "name": "IPhone X",
            "brand": "APPLE",
            "model_year": datetime.now().year
        }
        p_m = PhoneModel.objects.create(**phone_model)

        date_format='%Y-%m-%dT%H:%M:%S.%fZ'

        cls.data = {
            'phone_model': p_m,
            'author': author_instance,
            'comment': 'mycomment',
            'date_release': datetime.today(),
            'date_create': datetime.today(),
            'date_modify': datetime.today(),
        }
        cls.read_data = cls.data.copy()
        cls.read_data.update({
            'phone_model': phone_model,
            'author': author,
            'date_release': cls.read_data['date_release'].strftime(date_format),
            'date_create': cls.read_data['date_create'].strftime(date_format),
            'date_modify': cls.read_data['date_modify'].strftime(date_format),
        })
        cls.write_data = cls.data.copy()
        cls.write_data.update({
            'author': author_instance.id,
            'phone_model': p_m.id,
        })


    def test_read(self):
        serializer = PhoneReadSerializer(instance=Phone.objects.create(**self.data))
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

    def test_valid_write(self):
        serializer = PhoneWriteSerializer(data=self.write_data)
        serializer.is_valid()
        self.assertTrue(serializer.is_valid())
