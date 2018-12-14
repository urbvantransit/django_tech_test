# coding: utf8
from decimal import Decimal

from django.urls import reverse
from rest_framework.test import APITestCase

from apps.lines.factories import RouteFactory
from apps.users.test import CustomUserTestMixin
from apps.stations.factories import (LocationFactory, StationFactory)


# Test class for the List and create methods for Location Model
class LocationCreateTest(CustomUserTestMixin, APITestCase):

    url = reverse("locations:v1_list_create_location")
    username = 'admin'

    def test_list(self):
        LocationFactory()

        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
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


class LocationDetailTest(CustomUserTestMixin, APITestCase):
    """
        Test class for the detail methods for Location Model: Retrieve, update, destroy
    """

    def test_retrieve_successfully(self):
        """
            Retrieve test for Location Model API
        """
        st = LocationFactory()
        url = reverse("locations:v1_detail_location", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], st.id)

    def test_update_successfully(self):
        """
            Update unit test for Location Model API
        """
        st = LocationFactory()
        url = reverse("locations:v1_detail_location", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Decimal(response.data['latitude']), st.latitude)
        data = {
            "id": st.id,
            "name": st.name,
            "latitude": st.latitude + 10,
            "longitude": st.longitude
        }
        response = self.client.put(url, data=data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], st.id)
        self.assertEquals(Decimal(response.data['latitude']), st.latitude+10)

    def test_destroy_successfully(self):
        """
            Update unit test for Location Model API
        """
        st = LocationFactory()
        url = reverse("locations:v1_detail_location", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 204)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)


class StationListCreateTest(CustomUserTestMixin, APITestCase):
    """
        Test class for the List and create methods for Station Model
    """

    url = reverse("stations:v1_list_create_station")

    def test_list(self):
        StationFactory()
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        response = response.json()
        self.assertEquals(response['body'].get('count'), 1)

    def test_create_successfully(self):
        url_location = reverse("locations:v1_list_create_location")
        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }
        response = self.client.post(url_location, data, format='json')
        self.assertEquals(response.status_code, 201)
        location = response.data['body']['results'][0]['id']
        route = RouteFactory()
        data = {
            "location": location,
            "route": route.id,
            "order": 1,
            "is_active": True
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)


# Test class for the detail methods for Station Model: Retrieve, update, destroy
class StationDetailTest(CustomUserTestMixin, APITestCase):

    def test_retrieve_successfully(self):
        """
            Retrieve test for Station Model API
        """
        st = StationFactory()
        url = reverse("stations:v1_detail_station", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], st.id)

    def test_update_successfully(self):
        """
            Update unit test for Station Model API
        """
        st = StationFactory()
        url = reverse("stations:v1_detail_station", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['order'], st.order)
        # Test partial update
        data = {
            "order": st.order + 1,
        }
        response = self.client.patch(url, data=data)
        self.assertEquals(response.status_code, 200)
        # Test total update
        data = {
            "location": st.location.id,
            "route": st.route.id,
            "order": st.order + 2,
            "partial": True
        }
        response = self.client.put(url, data=data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['id'], st.id)
        self.assertEquals(response.data['order'], st.order+2)

    def test_destroy_successfully(self):
        """
            Update unit test for Station Model API
        """
        st = StationFactory()
        url = reverse("stations:v1_detail_station", kwargs={'pk': st.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 204)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
