# coding: utf8
from django.urls import reverse

from rest_framework.test import APITestCase

from apps.users.factories import (UserFactory, TokenFactory)
from apps.stations.factories import LocationFactory, StationFactory


class LocationCreateTest(APITestCase):

    url = reverse("locations:v1_list_create_location")

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list(self):
        LocationFactory()

        response = self.client.get(self.url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 1)

    def test_create_successfully(self):
        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)


class LocationManageTest(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_retrieve(self):
        location = LocationFactory()

        url = reverse("locations:v1_location_manage", kwargs={'pk': location.id})

        response = self.client.get(url, format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], location.id)

    def test_update(self):
        location = LocationFactory()

        data = {
            "name": "socks"
        }

        url = reverse("locations:v1_location_manage", kwargs={'pk': location.id})

        response = self.client.patch(url, data, format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['name'], "socks")

    def test_delete(self):
        location = LocationFactory()

        url = reverse("locations:v1_location_manage", kwargs={'pk': location.id})

        response = self.client.delete(url, format='json')

        self.assertEquals(response.status_code, 204)

        deleted = self.client.get(url, format='json')
        self.assertEquals(deleted.status_code, 404)


class StationCreateTest(APITestCase):

    url = reverse("stations:v1_list_create_station")

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list(self):
        StationFactory()

        response = self.client.get(self.url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 1)

    def test_create_successfully(self):
        location = LocationFactory()
        
        data = {
            "location": location.id,
            "order": 20,
            "is_active": True
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)


class StationManageTest(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_retrieve(self):
        station = StationFactory()

        url = reverse("stations:v1_station_manage", kwargs={'pk': station.id})

        response = self.client.get(url, format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], station.id)

    def test_update(self):
        station = StationFactory()

        data = {
            "order": 420
        }

        url = reverse("stations:v1_station_manage", kwargs={'pk': station.id})

        response = self.client.patch(url, data, format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['order'], 420)

    def test_delete(self):
        station = StationFactory()

        url = reverse("stations:v1_station_manage", kwargs={'pk': station.id})

        response = self.client.delete(url, format='json')

        self.assertEquals(response.status_code, 204)

        deleted = self.client.get(url, format='json')
        self.assertEquals(deleted.status_code, 404)
