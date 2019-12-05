import datetime

from rest_framework.test import APITestCase

from storage.api.phone_model.serializers import PhoneModelSerializer
from storage.models import PhoneModel


class PhoneModelSerializerTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.data = {
            "name": "IPhone X",
            "brand": "APPLE",
            "model_year": datetime.datetime.now().year
        }

    def test_read(self):
        serializer = PhoneModelSerializer(instance=PhoneModel.objects.create(**self.data))
        self.assertIn("id", serializer.data)
        self.assertEqual(serializer.data['id'], 1)
        for key, value in self.data.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, serializer.data)
                self.assertEqual(serializer.data[key], value)

    def test_valid_write(self):
        serializer = PhoneModelSerializer(data=self.data)

        self.assertTrue(serializer.is_valid())

    def test_invalid_model_year(self):
        data = self.data.copy()
        data["model_year"] = datetime.datetime.now().year + 1
        serializer = PhoneModelSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertIn("model_year", serializer.errors)
        self.assertEqual(serializer.errors["model_year"][0].code, 'max_value')

    # def test_renew_form_date_too_far_in_future(self):
    #     date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
    #     form_data = {'renewal_date': date}
    #     form = RenewBookForm(data=form_data)
    #     self.assertFalse(form.is_valid())
    #
    # def test_renew_form_date_today(self):
    #     date = datetime.date.today()
    #     form_data = {'renewal_date': date}
    #     form = RenewBookForm(data=form_data)
    #     self.assertTrue(form.is_valid())
    #
    # def test_renew_form_date_max(self):
    #     date = timezone.now() + datetime.timedelta(weeks=4)
    #     form_data = {'renewal_date': date}
    #     form = RenewBookForm(data=form_data)
    #     self.assertTrue(form.is_valid())
