# coding: utf-8
from random import randint

from django.urls import reverse

from rest_framework import status

from apps.lines.factories import LineFactory, RouteFactory
from apps.stations.factories import StationFactory
from apps.utils import APITestCaseWithClients


class RouteListCreateTest(APITestCaseWithClients):

    list_create_url = reverse("routes:v1_list_create_route")

    @classmethod
    def setUpTestData(cls):
        super(cls, RouteListCreateTest).setUpTestData()

    def test_list(self):
        items = randint(1, 100)
        for i in range(items):
            RouteFactory()

        response = self.auth_client.get(self.list_create_url)
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content['body'].get('count'), items)

    def test_create_successfully(self):
        line = LineFactory()
        station_items = randint(1, 100)
        stations = []
        for i in range(station_items):
            station = StationFactory()
            stations.append(station.id)

        data = {
            "line": line.id,
            "stations": stations,
            "direction": False,
            "is_active": False,
        }

        response = self.auth_client.post(
            self.list_create_url, data, format='json')
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content['body'].get('count'), 1)
        self.assertDictContainsSubset({
            "direction": False,
            "is_active": False
        }, content['body'].get('results')[0])
        self.assertDictContainsSubset({
            "id": line.id
        }, content['body'].get('results')[0].get('line'))
