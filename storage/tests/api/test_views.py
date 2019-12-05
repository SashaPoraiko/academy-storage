from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group

from rest_framework.test import APIClient, APITestCase

from storage.models import PhoneModel


class PhoneModelListViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_phone_models = 13

        for phone_model_num in range(number_of_phone_models):
            PhoneModel.objects.create(name='somePMname', brand='Apple', model_year=2017, )

        username = 'test user'
        password = 'password'

        group = Group.objects.create(name='managers')
        cls.user = User.objects.create(username=username, password=make_password(password))
        cls.user.groups.set([group])

        # cls.client.force_authenticate(cls.user)
        # todo rewrite force_authenticate to credentials method
        # cls.headers = {
        #     'Authorization': 'Bearer %s' % cls.api_client.post('/api/auth/token/', {
        #         "username": username,
        #         "password": password,
        #     }).data['access']
        # }
        # cls.api_client.credentials(HTTP_AUTORIZATION=cls.headers['Authorization'])

    def test_view_url_exists_at_desired_location(self):
        self.client.force_authenticate(self.user)
        resp = self.client.get('/api/v1/phone-model/')
        self.assertEqual(resp.status_code, 200)

    def test_pagination_is_ten(self):
        self.client.force_authenticate(self.user)
        resp = self.client.get('/api/v1/phone-model/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('count' in resp.data)
        self.assertEqual(resp.data['count'], 13)
        self.assertEqual(len(resp.data['results']), 10)

    def test_lists_all_authors(self):
        self.client.force_authenticate(self.user)
        resp = self.client.get('/api/v1/phone-model/', {'page': 2})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('count' in resp.data)
        self.assertEqual(resp.data['count'], 13)
        self.assertEqual(len(resp.data['results']), 3)
