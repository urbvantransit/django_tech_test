# coding: utf8
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.users.factories import UserFactory, TokenFactory
from .factories import LocationFactory, StationFactory


class LocationViewSetTest(APITestCase):
    url = reverse("locationmodel-list")

    def setUp(self):
        # TODO factor out
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

    def test_non_empty_create(self):
        LocationFactory.create_batch(4)

        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)

    def test_detail(self):
        loc = LocationFactory()
        url = reverse('locationmodel-detail', kwargs={'pk': loc.id})
        response = self.client.get(url).json()
        self.assertEquals(loc.name, response['name'])


class StationCRUDTest(APITestCase):
    url = reverse('stationmodel-list')

    def setUp(self):
        # TODO factor out
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list_create(self):
        response = self.client.get(self.url)
        response = response.json()
        self.assertEquals(response['body'].get('count'), 0)

        loc = LocationFactory()
        data = {
            "location": reverse('locationmodel-detail', kwargs={'pk': loc.id}),
            "order": 1
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)

        response = self.client.get(self.url)
        response = response.json()
        self.assertEquals(response['body'].get('count'), 1)

    def test_update(self):
        """Change the order of a factory Station"""
        # test initial order
        sta = StationFactory()
        response = self.client.get(self.url)
        response_dict = response.json()
        self.assertEquals(response_dict['body']['count'], 1)
        self.assertEquals(response_dict['body']['results'][0]['order'], sta.order)
        # get Station to patch
        detail_url = reverse('stationmodel-detail', kwargs={'pk': sta.id})
        response = self.client.patch(detail_url, data={'order': 101}, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['order'], 101)

    def test_delete(self):
        StationFactory.create_batch(10)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        # get which station to delete
        delete_sta = response.json()['body']['results'][0]['url']
        response = self.client.delete(delete_sta)
        self.assertEquals(response.status_code, 204)
        # ensure it was deleted
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['body']['count'], 9)
