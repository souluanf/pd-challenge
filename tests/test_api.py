from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase

User = get_user_model()


class TestApiDrf(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.password = '123'
        cls.user = User.objects.create_user(
            'testeapi',
            'testeapi@testeapi.com',
            cls.password,
        )
        cls.client = APIClient()
        url = reverse('token_obtain_pair')
        data = {
            'username': cls.user.username,
            'password': cls.password
        }
        response = cls.client.post(url, data=data)
        cls.tokens = response.data

    # ---------TESTS----------#

    def test_create_place(self):
        url = reverse('api-root:places-list')
        data = {
            "name": "Lagoa Azul",
            "slug": "lagoa-azul",
            "city": "São Paulo",
            "state": "SP"
        }

        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.post(url, data, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_places(self):
        url = reverse('api-root:places-list')
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list_place_by_name(self):
        url = reverse('search-name', args=['Fatec ZS'])
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_place_by_slug(self):
        url = reverse('search-slug', args=['fatec-zs'])
        auth = 'Bearer {0}'.format(self.tokens['access'])
        response = self.client.get(url, HTTP_AUTHORIZATION=auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
