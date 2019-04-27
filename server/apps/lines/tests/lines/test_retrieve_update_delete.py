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

        response = self.auth_admin_client.get(retrieve_update_delete)
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
            "name": "test_name_2",
            "color": "0088FF"
        }

        response = self.auth_admin_client.patch(
            retrieve_update_delete, data, format='json')
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content['body'].get('count'), 1)
        self.assertDictContainsSubset(data, content['body'].get('results')[0])

    def test_delete_by_pk(self):
        line = LineFactory()
        retrieve_update_delete = reverse(
            "lines:v1_retrieve_update_delete_line",
            kwargs={
                "pk": line.id
            })

        response = self.auth_admin_client.delete(retrieve_update_delete)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_driver_retrieve_by_pk(self):
        line = LineFactory()

        items = randint(1, 100)
        for i in range(items):
            LineFactory()

        retrieve_update_delete = reverse(
            "lines:v1_retrieve_update_delete_line",
            kwargs={
                "pk": line.id
            })

        response = self.auth_driver_client.get(retrieve_update_delete)
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content['body'].get('count'), 1)

    def test_driver_update_by_pk(self):
        line = LineFactory()
        retrieve_update_delete = reverse(
            "lines:v1_retrieve_update_delete_line",
            kwargs={
                "pk": line.id
            })

        data = {
            "name": "test_name_2",
            "color": "0088FF"
        }

        response = self.auth_driver_client.patch(
            retrieve_update_delete, data, format='json')
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(content['body'].get('count'), 1)
        self.assertDictContainsSubset(data, content['body'].get('results')[0])

    def test_driver_delete_by_pk_does_not_have_permission(self):
        line = LineFactory()
        retrieve_update_delete = reverse(
            "lines:v1_retrieve_update_delete_line",
            kwargs={
                "pk": line.id
            })

        response = self.auth_driver_client.delete(retrieve_update_delete)
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(content['detail'],
                          self.USER_DOES_NOT_HAVE_PERMISSION)

    def test_user_retrieve_by_pk(self):
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

    def test_user_update_by_pk_does_not_have_permission(self):
        line = LineFactory()
        retrieve_update_delete = reverse(
            "lines:v1_retrieve_update_delete_line",
            kwargs={
                "pk": line.id
            })

        data = {
            "name": "test_name_2",
            "color": "0088FF"
        }

        response = self.auth_client.patch(
            retrieve_update_delete, data, format='json')
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(content['detail'],
                          self.USER_DOES_NOT_HAVE_PERMISSION)

    def test_user_delete_by_pk_does_not_have_permission(self):
        line = LineFactory()
        retrieve_update_delete = reverse(
            "lines:v1_retrieve_update_delete_line",
            kwargs={
                "pk": line.id
            })

        response = self.auth_client.delete(retrieve_update_delete)
        content = response.json()

        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(content['detail'],
                          self.USER_DOES_NOT_HAVE_PERMISSION)
