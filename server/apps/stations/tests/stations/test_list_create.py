# coding: utf-8
from random import randint

from django.urls import reverse

from rest_framework import status

from apps.stations.factories import LocationFactory, StationFactory
from apps.utils import APITestCaseWithClients


class StationListCreateTest(APITestCaseWithClients):

    list_create_url = reverse("stations:v1_list_create_station")

    @classmethod
    def setUpTestData(cls):
        super(cls, StationListCreateTest).setUpTestData()

    def test_list(self):
        items = randint(1, 100)
        for i in range(items):
            StationFactory()

        response = self.auth_client.get(self.list_create_url)
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content['body'].get('count'), items)

    def test_create_successfully(self):
        location = LocationFactory()

        data = {
            "location": location.id,
            "order": 1,
            "is_active": False
        }

        response = self.auth_client.post(
            self.list_create_url, data, format='json')
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content['body'].get('count'), 1)
        self.assertDictContainsSubset({
            "order": 1,
            "is_active": False
        }, content['body'].get('results')[0])
        self.assertDictContainsSubset({
            "id": location.id
        }, content['body'].get('results')[0].get('location'))
