from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group

from rest_framework.test import APITestCase


class PhoneListViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        username = 'test user'
        password = 'password'

        group = Group.objects.create(name='managers')
        cls.user = User.objects.create(username=username, password=make_password(password))
        cls.user.groups.set([group])

    def test_view_url_exists_at_desired_location(self):
        self.client.force_authenticate(self.user)
        resp = self.client.get('/api/v1/phone/')
        self.assertEqual(resp.status_code, 200)

    def test_lists_all_phones(self):
        self.client.force_authenticate(self.user)
        resp = self.client.get('/api/v1/phone/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('count' in resp.data)
