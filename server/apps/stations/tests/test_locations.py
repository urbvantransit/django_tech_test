# coding: utf-8
from django.urls import reverse

from rest_framework import status

from apps.stations.factories import LocationFactory
from apps.utils import APITestCaseWithClients


class LocationListCreateTest(APITestCaseWithClients):

    url = reverse("locations:v1_list_create_location")

    @classmethod
    def setUpTestData(cls):
        super(cls, LocationListCreateTest).setUpTestData()

    def test_list(self):
        LocationFactory()

        response = self.auth_client.get(self.url)
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content['body'].get('count'), 1)

    def test_create_successfully(self):
        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }

        response = self.auth_client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
