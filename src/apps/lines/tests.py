# coding: utf8
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .factories import LineFactory, RouteFactory
from ..users.factories import TokenFactory, UserFactory


class BaseLineTest():

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )


class LineTest(BaseLineTest, APITestCase):
    url = reverse("lines:v1_list_line")

    def test_list_successfully(self):
        LineFactory()
        response = self.client.get(self.url)
        response_data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['body'].get('count'), 1)

    def test_create_successfully(self):
        data = {
            "name": 'Tacubaya',
            "color": 'Naranja'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_successfully(self):
        line = LineFactory()
        url = reverse(
            "lines:v1_detail_line", kwargs={'pk': line.id}
        )
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['body']['results'][0]['id'], line.id
        )

    def test_update_successfully(self):
        line = LineFactory()
        url = reverse(
            "lines:v1_detail_line", kwargs={'pk': line.id}
        )
        data = {"name": "San Pedro de los Pinos"}
        response = self.client.patch(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['body']['results'][0]['name'], data['name']
        )

    def test_delete_successfully(self):
        line = LineFactory()
        url = reverse(
            "lines:v1_detail_line", kwargs={'pk': line.id}
        )
        response = self.client.delete(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


class RouteTest(BaseLineTest, APITestCase):
    url = reverse("routes:v1_list_route")

    def test_list_successfully(self):
        RouteFactory()
        response = self.client.get(self.url)
        response_data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['body'].get('count'), 1)

    def test_create_successfully(self):
        line = LineFactory()
        data = {
            "is_active": True,
            "direction": True,
            "line": line.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_successfully(self):
        route = RouteFactory()
        url = reverse(
            "routes:v1_detail_route", kwargs={'pk': route.id}
        )
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['body']['results'][0]['id'], route.id
        )

    def test_update_successfully(self):
        route = RouteFactory()
        url = reverse(
            "routes:v1_detail_route", kwargs={'pk': route.id}
        )
        data = {"direction": False}
        response = self.client.patch(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data['body']['results'][0]['direction'])

    def test_delete_successfully(self):
        route = RouteFactory()
        url = reverse(
            "routes:v1_detail_route", kwargs={'pk': route.id}
        )
        response = self.client.delete(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
