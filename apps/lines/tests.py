from django.urls import reverse
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory
from apps.users.factories import (
    UserFactory,
    UserStaffFactory,
    UserSuperadminFactory,
    TokenFactory,
)
from .factories import LineFactory, RouteFactory
from apps.stations.factories import StationFactory

factory = APIRequestFactory()


class LineCreateTest(APITestCase):

    url_list = reverse("line-all")
    url_create = reverse("line-create")
    url_detail = reverse("line-detail", kwargs={"pk": "pk"})
    url_delete = reverse("line-delete", kwargs={"pk": "pk"})

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(AUTHORIZATION="Urbvan {}".format(self.user_token.key))

    def test_list(self):
        LineFactory()

        response = self.client.get(self.url_list)
        response = response.json()

        self.assertEquals(len(response), 1)

    def test_create_successfully(self):
        self.user = UserSuperadminFactory()
        self.user_token = TokenFactory(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token))
        data = {"name": "line", "color": "rojo"}

        response = self.client.post(self.url_create, data, format="json")
        self.assertEquals(response.status_code, 201)

    def test_create_forbidden(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token))
        data = {"name": "line", "color": "rojo"}

        response = self.client.post(self.url_create, data, format="json")
        self.assertEquals(response.status_code, 403)

    def test_detail_successfully(self):
        self.user = UserStaffFactory()
        self.user_token = TokenFactory(user=self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

        line = LineFactory()
        data = {"pk": line.id}
        url = str(self.url_detail).replace("pk", data["pk"])
        response = self.client.get(url, data, format="json")
        self.assertEquals(response.status_code, 200)

    def test_detail_forbidden(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

        line = LineFactory()
        data = {"pk": line.id}
        url = str(self.url_detail).replace("pk", data["pk"])
        response = self.client.get(url, data, format="json")
        self.assertEquals(response.status_code, 403)

    def test_delete_successfully(self):
        self.user = UserSuperadminFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )
        line = LineFactory()
        data = {"pk": line.id}

        # Get with success the element
        url = str(self.url_detail).replace("pk", data["pk"])
        response = self.client.get(url, data, format="json")
        self.assertEquals(response.status_code, 200)

        # Delete element and check
        url = str(self.url_delete).replace("pk", data["pk"])
        response = self.client.delete(url, data, format="json")
        self.assertEquals(response.status_code, 204)

        # Not found element
        url = str(self.url_detail).replace("pk", data["pk"])
        response = self.client.get(url, data, format="json")
        self.assertEquals(response.status_code, 404)


class RouteCreateTest(APITestCase):

    url_list = reverse("routes-all")
    url_create = reverse("routes-create")
    url_detail = reverse("routes-detail", kwargs={"pk": "pk"})
    url_delete = reverse("routes-delete", kwargs={"pk": "pk"})

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list(self):
        RouteFactory()

        response = self.client.get(self.url_list)
        response = response.json()

        self.assertEquals(len(response), 1)

    def test_create_successfully(self):
        self.user = UserSuperadminFactory()
        self.user_token = TokenFactory(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token))

        line = LineFactory()
        station = StationFactory()

        data = {
            "line": line.id,
            "stations": [station.id],
            "direction": True,
            "is_active": True,
        }

        response = self.client.post(self.url_create, data, format="json")
        self.assertEquals(response.status_code, 201)

    def test_create_forbidden(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token))

        line = LineFactory()
        station = StationFactory()

        data = {
            "line": line.id,
            "stations": [station.id],
            "direction": True,
            "is_active": True,
        }

        response = self.client.post(self.url_create, data, format="json")
        self.assertEquals(response.status_code, 403)

    def test_detail_successfully(self):
        self.user = UserStaffFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

        route = RouteFactory()
        data = {"pk": route.id}
        url = str(self.url_detail).replace("pk", data["pk"])
        response = self.client.get(url, data, format="json")
        self.assertEquals(response.status_code, 200)

    def test_detail_forbidden(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

        route = RouteFactory()
        data = {"pk": route.id}
        url = str(self.url_detail).replace("pk", data["pk"])
        response = self.client.get(url, data, format="json")
        self.assertEquals(response.status_code, 403)

    def test_delete_successfully(self):
        self.user = UserSuperadminFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )
        route = RouteFactory()
        data = {"pk": route.id}

        # Get with success the element
        url = str(self.url_detail).replace("pk", data["pk"])
        response = self.client.get(url, data, format="json")
        self.assertEquals(response.status_code, 200)

        # Delete element and check
        url = str(self.url_delete).replace("pk", data["pk"])
        response = self.client.delete(url, data, format="json")
        self.assertEquals(response.status_code, 204)

        # Not found element
        url = str(self.url_detail).replace("pk", data["pk"])
        response = self.client.get(url, data, format="json")
        self.assertEquals(response.status_code, 404)
