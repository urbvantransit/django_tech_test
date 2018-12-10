# coding: utf8
from unittest.mock import patch

from django.urls import reverse

from rest_framework.test import APITestCase

from apps.users.factories import (UserFactory, TokenFactory)
from apps.stations.factories import (LocationFactory, )


class LocationCreateTest(APITestCase):

    url = reverse("locations:v1_list_create_location")

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)
        self.user.is_staff = True
        self.user.save()

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

    def test_retrieve_successfully(self):
        LocationFactory()

        response_1 = self.client.get(self.url)
        response_1 = response_1.json()
        location = response_1['body']['results'][0]

        response_2 = self.client.get(self.url + location['id'])
        response_2 = response_2.json()
        self.assertEquals(response_2['body'].get('count'), 1)

    def test_update_successfully(self):
        LocationFactory()
        data = {
            "name": "Urbvan!",
            "latitude": 19.388401,
            "longitude": -99.227358
        }

        response_1 = self.client.get(self.url)
        response_1 = response_1.json()
        location = response_1['body']['results'][0]

        response_2 = self.client.put(self.url + location['id'], data, format='json')
        self.assertEquals(response_2.status_code, 200)
        
        response_2 = response_2.json()
        self.assertEquals(response_2['body']['results'][0]['name'], data['name'])

    def test_delete_successfully(self):
        LocationFactory()

        response_1 = self.client.get(self.url)
        response_1 = response_1.json()
        location = response_1['body']['results'][0]

        response_2 = self.client.delete(self.url + location['id'], format='json')
        self.assertEquals(response_2.status_code, 204)

    def test_model_crud_permissions_basic(self):
        # 'Passenger' Users (the default users in the Factory) are not allowed to
        # delete the instances of Location, remove the staff status of the user
        # and test the denial
        self.user.is_staff = False
        self.user.save()
        LocationFactory()

        response_1 = self.client.get(self.url)
        response_1 = response_1.json()

        location = response_1['body']['results'][0]

        response_2 = self.client.delete(self.url + location['id'], format='json')
        self.assertEquals(response_2.status_code, 403)

        # 'Passenger' Users are allowed to retrieve, test the success
        response_3 = self.client.get(self.url)
        response_3 = response_3.json()

        self.assertEquals(response_3['body'].get('count'), 1)

        # Return the User object to its 'original' state
        self.user.is_staff = True
        self.user.save()

    @patch('apps.stations.models.LocationModel.MODEL_CRUD_PERMISSIONS', new=None)
    def test_model_crud_permissions_no_config(self):
        """
        Test MCP is ignored
        """
        self.user.is_staff = False
        self.user.save()
        LocationFactory()

        response_1 = self.client.get(self.url)
        response_1 = response_1.json()
        location = response_1['body']['results'][0]

        response_2 = self.client.delete(self.url + location['id'], format='json')
        self.assertEquals(response_2.status_code, 204)

