# coding: utf8
from django.test import TestCase
# coding: utf8
from django.urls import reverse

from rest_framework.test import APITestCase

from apps.users.factories import (UserFactory, TokenFactory)
from apps.stations.factories import StationFactory
from .factories import LineFactory, RouteFactory


class LineCreateTest(APITestCase):

    url = reverse("lines:v1_list_create_line")

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list(self):
        LineFactory()

        response = self.client.get(self.url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 1)

    def test_create_successfully(self):
        data = {
            "name": "Gosh Darn",
            "color": "colorful",
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)


class LineManageTest(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_retrieve(self):
        line = LineFactory()

        url = reverse("lines:v1_line_manage", kwargs={'pk': line.id})

        response = self.client.get(url, format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], line.id)

    def test_update(self):
        line = LineFactory()

        data = {
            "name": "socks"
        }

        url = reverse("lines:v1_line_manage", kwargs={'pk': line.id})

        response = self.client.patch(url, data, format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['name'], "socks")

    def test_delete(self):
        line = LineFactory()

        url = reverse("lines:v1_line_manage", kwargs={'pk': line.id})

        response = self.client.delete(url, format='json')

        self.assertEquals(response.status_code, 204)

        deleted = self.client.get(url, format='json')
        self.assertEquals(deleted.status_code, 404)


class RouteCreateTest(APITestCase):

    url = reverse("routes:v1_list_create_route")

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list(self):
        RouteFactory.create(stations=(StationFactory(),))

        response = self.client.get(self.url)
        response = response.json()
        print(response)

        self.assertEquals(response['body'].get('count'), 1)

    def test_create_successfully(self):
        line= LineFactory()
        station1 = StationFactory()

        data = {
            "line": line.id,
            "stations": [station1.id,],
            "direction": True,
            "is_active": True
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)


class StationManageTest(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_retrieve(self):
        route = RouteFactory.create(stations=(StationFactory(),))

        url = reverse("routes:v1_route_manage", kwargs={'pk': route.id})

        response = self.client.get(url, format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], route.id)

    def test_update(self):
        route = RouteFactory.create(stations=(StationFactory(),))

        data = {
            "direction": False
        }

        url = reverse("routes:v1_route_manage", kwargs={'pk': route.id})

        response = self.client.patch(url, data, format='json')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['direction'], False)

    def test_delete(self):
        route = RouteFactory.create(stations=(StationFactory(),))

        url = reverse("routes:v1_route_manage", kwargs={'pk': route.id})

        response = self.client.delete(url, format='json')

        self.assertEquals(response.status_code, 204)

        deleted = self.client.get(url, format='json')
        self.assertEquals(deleted.status_code, 404)
