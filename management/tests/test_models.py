from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.

from ..models import Feedback


class FeedbackModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.feedback = Feedback.objects.create(message='Big', name='Bob', email='asd', phone='2d')

    # def test_date_of_death_label(self):
    #     author = Author.objects.get(id=1)
    #     field_label = author._meta.get_field('date_of_death').verbose_name
    #     self.assertEquals(field_label, 'died')
    #
    def test_message_max_length(self):
        max_length = self.feedback._meta.get_field('message').max_length
        self.assertEquals(max_length, 2048)

    def test_phone_max_length(self):
        max_length = self.feedback._meta.get_field('phone').max_length
        self.assertEquals(max_length, 50)

    def test_name_max_length(self):
        max_length = self.feedback._meta.get_field('name').max_length
        self.assertEquals(max_length, 80)

    def test_email_max_length(self):
        max_length = self.feedback._meta.get_field('email').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_last_name_comma_first_name(self):
        expected_object_name = '%s %s %s' % (self.feedback.name, self.feedback.email, self.feedback.phone)
        self.assertEquals(expected_object_name, str(self.feedback))
