# coding: utf-8
from random import randint

from django.urls import reverse

from rest_framework import status

from apps.lines.factories import LineFactory
from apps.utils import APITestCaseWithClients


class LineRetrieveUpdateDelete(APITestCaseWithClients):

    @classmethod
    def setUpTestData(cls):
        super(cls, LineRetrieveUpdateDelete).setUpTestData()

    def test_retrieve_by_pk(self):
        line = LineFactory()

        items = randint(1, 100)
        for i in range(items):
            LineFactory()

        retrieve_update_delete = reverse(
            "lines:v1_retrieve_update_delete_line",
            kwargs={
                "pk": line.id
            })

        response = self.auth_client.get(retrieve_update_delete)
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content['body'].get('count'), 1)

    def test_update_by_pk(self):
        line = LineFactory()
        retrieve_update_delete = reverse(
            "lines:v1_retrieve_update_delete_line",
            kwargs={
                "pk": line.id
            })

        data = {
            "order": 2
        }

        response = self.auth_client.patch(
            retrieve_update_delete, data, format='json')
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content['body'].get('count'), 1)

    def test_delete_by_pk(self):
        line = LineFactory()
        retrieve_update_delete = reverse(
            "lines:v1_retrieve_update_delete_line",
            kwargs={
                "pk": line.id
            })

        response = self.auth_client.delete(retrieve_update_delete)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
