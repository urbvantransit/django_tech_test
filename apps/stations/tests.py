from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase

from apps.users.factories import (UserFactory, TokenFactory)
from apps.stations.factories import LocationFactory


class LocationReadTest(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list(self):
        url = reverse("read-locations-list")
        LocationFactory()
        LocationFactory()

        response = self.client.get(url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 2)

    def test_detail(self):
        LocationFactory()
        location = LocationFactory()
        url = reverse("read-locations-detail", kwargs={'pk': location.id})

        response = self.client.get(url)
        response = response.json()
        self.assertEquals(response['body'].get('count'), 1)


class LocationWriteTest(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_create_successfully(self):
        url = reverse("write-locations-list")
        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }

        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_update_successfully(self):
        location = LocationFactory()
        url = reverse("write-locations-detail", kwargs={'pk': location.id})
        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }

        response = self.client.patch(url, data, format='json')
        content = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(set(data).issubset(set(content['body'].get('results')[0])))

    def test_delete_successfully(self):
        location = LocationFactory()
        url = reverse("write-locations-detail", kwargs={'pk': location.id})

        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
