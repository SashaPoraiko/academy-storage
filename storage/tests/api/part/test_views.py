from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group

from rest_framework.test import APITestCase

from storage.models import Part


class PartModelListViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_parts = 13

        for part in range(number_of_parts):
            Part.objects.create(name='somePartname', condition=5, )

        username = 'test user'
        password = 'password'

        group = Group.objects.create(name='managers')
        cls.user = User.objects.create(username=username, password=make_password(password))
        cls.user.groups.set([group])

    def test_view_url_exists_at_desired_location(self):
        self.client.force_authenticate(self.user)
        resp = self.client.get('/api/v1/part/')
        self.assertEqual(resp.status_code, 200)

    def test_lists_all_parts(self):
        self.client.force_authenticate(self.user)
        resp = self.client.get('/api/v1/part/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('count' in resp.data)

    def test_pagination_is_ten(self):
        self.client.force_authenticate(self.user)
        resp = self.client.get('/api/v1/part/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('count' in resp.data)
        self.assertEqual(resp.data['count'], 13)
        self.assertEqual(len(resp.data['results']), 10)
