# coding: utf-8
from random import randint

from django.urls import reverse

from rest_framework import status

from apps.lines.factories import LineFactory
from apps.utils import APITestCaseWithClients


class LineListCreateTest(APITestCaseWithClients):

    url = reverse("lines:v1_list_create_line")

    @classmethod
    def setUpTestData(cls):
        super(cls, LineListCreateTest).setUpTestData()

    def test_list(self):
        items = randint(1, 100)
        for i in range(items):
            LineFactory()

        response = self.auth_admin_client.get(self.url)
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content['body'].get('count'), items)

    def test_create_successfully(self):
        data = {
            "name": "test_name",
            "color": "FF00AA"
        }

        response = self.auth_admin_client.post(
            self.url, data, format='json')
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(content['body'].get('count'), 1)
        self.assertDictContainsSubset(data, content['body'].get('results')[0])

    def test_create_by_driver_does_not_have_permission(self):
        data = {
            "name": "test_name",
            "color": "FF00AA"
        }

        response = self.auth_driver_client.post(self.url, data, format='json')
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(content['detail'],
                          self.USER_DOES_NOT_HAVE_PERMISSION)

    def test_create_by_user_does_not_have_permission(self):
        data = {
            "name": "test_name",
            "color": "FF00AA"
        }

        response = self.auth_client.post(self.url, data, format='json')
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(content['detail'],
                          self.USER_DOES_NOT_HAVE_PERMISSION)
