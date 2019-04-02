# coding: utf8
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .factories import LocationFactory, StationFactory
from ..users.factories import TokenFactory, UserFactory


class BaseStationsTest():

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )


class LocationTest(BaseStationsTest, APITestCase):
    url = reverse("locations:v1_list_location")

    def test_list_successfully(self):
        LocationFactory()
        response = self.client.get(self.url)
        response_data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['body'].get('count'), 1)

    def test_create_successfully(self):
        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_successfully(self):
        location = LocationFactory()
        url = reverse(
            "locations:v1_detail_location", kwargs={'pk': location.id}
        )
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['body']['results'][0]['id'], location.id
        )

    def test_update_successfully(self):
        location = LocationFactory()
        url = reverse(
            "locations:v1_detail_location", kwargs={'pk': location.id}
        )
        data = {"name": "New name"}
        response = self.client.patch(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['body']['results'][0]['name'], data['name']
        )

    def test_delete_successfully(self):
        location = LocationFactory()
        url = reverse(
            "locations:v1_detail_location", kwargs={'pk': location.id}
        )
        response = self.client.delete(url, format='json')
        self.assertEquals(
            response.status_code, status.HTTP_204_NO_CONTENT
        )


class StationTest(BaseStationsTest, APITestCase):
    url = reverse("stations:v1_list_station")

    def test_list_successfully(self):
        StationFactory()
        response = self.client.get(self.url)
        response_data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response_data['body'].get('count'), 1)

    def test_create_successfully(self):
        location = LocationFactory()
        data = {
            "order": "3",
            "is_active": False,
            "location": location.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_successfully(self):
        station = StationFactory()
        url = reverse(
            "stations:v1_detail_station", kwargs={'pk': station.id}
        )
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['body']['results'][0]['id'], station.id
        )

    def test_update_successfully(self):
        station = StationFactory()
        url = reverse(
            "stations:v1_detail_station", kwargs={'pk': station.id}
        )
        data = {'order': '7'}
        response = self.client.patch(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['body']['results'][0]['order'], data['order']
        )

    def test_delete_successfully(self):
        station = StationFactory()
        url = reverse(
            "stations:v1_detail_station", kwargs={'pk': station.id}
        )
        response = self.client.delete(url, format='json')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
