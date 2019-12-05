from django.test import TestCase

# Create your tests here.

from storage.models import PhoneModel
from django.urls import reverse


class PhoneModelListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_phone_models = 13

        for phone_model_num in range(number_of_phone_models):
            PhoneModel.objects.create(name='somePMname', brand='Apple', model_year=2017, )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/storage/phone-model/')
        self.assertEqual(resp.status_code, 200)

    # def test_view_url_accessible_by_name(self):
    #     resp = self.client.get(reverse('phone-model'))
    #     self.assertEqual(resp.status_code, 200)
    #
    # def test_pagination_is_ten(self):
    #     resp = self.client.get(reverse('phone-model'))
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertTrue('is_paginated' in resp.context)
    #     self.assertTrue(resp.context['is_paginated'] == True)
    #     self.assertTrue(len(resp.context['phone-model_list']) == 10)
    #
    # def test_lists_all_authors(self):
    #     # Get second page and confirm it has (exactly) remaining 3 items
    #     resp = self.client.get(reverse('phone-model') + '?page=2')
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertTrue('is_paginated' in resp.context)
    #     self.assertTrue(resp.context['is_paginated'] == True)
    #     self.assertTrue(len(resp.context['phone-model']) == 3)
