from django.contrib.auth.models import User
from django.test import TestCase

from storage.models import Phone, PhoneModel
from datetime import datetime


class PhoneModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = User.objects.create_superuser('username', 'theemail123@gmail.com', 'Superpassword123')
        phone_model = {
            "name": "IPhone X",
            "brand": "APPLE",
            "model_year": datetime.now().year
        }
        p_m = PhoneModel.objects.create(**phone_model)

        cls.phone = Phone.objects.create(author=author, phone_model=p_m, comment='theComment', condition=5,
                                         date_release=datetime.now(),
                                         date_create=datetime.now(), date_modify=datetime.now(), status='Active')

    def test_fields_required_length(self):
        max_length_comment = self.phone._meta.get_field('comment').max_length
        max_length_status = self.phone._meta.get_field('status').max_length
        self.assertEquals(max_length_comment, 255)
        self.assertEquals(max_length_status, 30)

    def test_condition_is_valid(self):
        cond = self.phone.condition
        self.assertTrue(0 < cond <= 10)

    def test_status_is_valid(self):
        status = self.phone.status
        self.assertTrue(status)
        self.assertEqual('Active', status)
