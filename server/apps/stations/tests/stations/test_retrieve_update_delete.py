# coding: utf-8
from random import randint

from django.urls import reverse

from rest_framework import status

from apps.stations.factories import LocationFactory, StationFactory
from apps.utils import APITestCaseWithClients


class StationRetrieveUpdateDelete(APITestCaseWithClients):

    @classmethod
    def setUpTestData(cls):
        super(cls, StationRetrieveUpdateDelete).setUpTestData()

    def test_retrieve_by_pk(self):
        station = StationFactory()
        items = randint(1, 100)
        for i in range(items):
            StationFactory()

        retrieve_update_delete = reverse(
            "stations:v1_retrieve_update_delete_station",
            kwargs={
                "pk": station.id
            })

        response = self.auth_client.get(retrieve_update_delete)
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content['body'].get('count'), 1)

    def test_update_by_pk(self):
        station = StationFactory()
        retrieve_update_delete = reverse(
            "stations:v1_retrieve_update_delete_station",
            kwargs={
                "pk": station.id
            })

        location = LocationFactory()

        data = {
            "location": location.id,
            "order": 1,
            "is_active": False
        }

        response = self.auth_client.patch(
            retrieve_update_delete, data, format='json')
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content['body'].get('count'), 1)
        self.assertDictContainsSubset({
            "order": 1,
            "is_active": False
        }, content['body'].get('results')[0])
        self.assertDictContainsSubset({
            "id": location.id
        }, content['body'].get('results')[0].get('location'))

    def test_delete_by_pk(self):
        station = StationFactory()
        retrieve_update_delete = reverse(
            "stations:v1_retrieve_update_delete_station",
            kwargs={
                "pk": station.id
            })

        response = self.auth_client.delete(retrieve_update_delete)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
