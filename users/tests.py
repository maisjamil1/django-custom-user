from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CustomUser


class UserTests(TestCase):

    def setUp(self):
            self.user = get_user_model().objects.create_user(
                username='mais',
                email='maisjamil17118@gmail.com',
                password='1234'
            )


    def test_home_status(self):
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
    

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'home.html'
        self.assertTemplateUsed(response, actual)

    # def test_details_view(self):
    #     response = self.client.get(reverse('signup', args='1'))
    #     self.assertEqual(response.status_code, 200)

    def test_signup_page_url_and_template(self):
        response = self.client.get("/users/signup/")
        self.assertEqual(response.status_code, 200)
