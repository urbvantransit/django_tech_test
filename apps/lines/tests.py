# coding: utf8
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.users.factories import UserFactory
from . import factories


class LineCRUDTest(APITestCase):
    url = reverse('linemodel-list')

    def setUp(self):
        self.client.force_login(UserFactory())

    def test_list_create(self):
        response = self.client.get(self.url)
        response = response.json()
        self.assertEquals(response['body'].get('count'), 0)

        line_data = {'name': 'ruby rod supegreen', 'color': '#8c8832'}
        response = self.client.post(self.url, line_data, format='json')
        self.assertEquals(response.status_code, 201)

        response = self.client.get(self.url)
        response = response.json()
        self.assertEquals(response['body'].get('count'), 1)

    def test_update(self):
        """test PATCH"""
        # test initial order
        line = factories.LineFactory()
        response = self.client.get(self.url)
        response_dict = response.json()
        self.assertEquals(response_dict['body']['count'], 1)
        self.assertEquals(response_dict['body']['results'][0]['color'], line.color)
        # get uri to patch
        detail_url = reverse('linemodel-detail', kwargs={'pk': line.id})
        response = self.client.patch(detail_url, data={'color': '#8c8832'}, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['color'], '#8c8832')

    def test_delete(self):
        factories.LineFactory.create_batch(10)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        # get which station to delete
        delete_obj = response.json()['body']['results'][0]['url']
        response = self.client.delete(delete_obj)
        self.assertEquals(response.status_code, 204)
        # ensure it was deleted
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['body']['count'], 9)


class RouteCRUDTest(APITestCase):
    url = reverse('routemodel-list')

    def setUp(self):
        self.client.force_login(UserFactory())

    def test_list_create(self):
        line = factories.LineFactory()
        sta = factories.StationFactory()
        line_url = reverse('linemodel-detail', kwargs={'pk': line.id})
        sta_url = reverse('stationmodel-detail', kwargs={'pk': sta.id})

        route_data = {
            'line': line_url,
            'stations': [sta_url, sta_url]
        }
        response = self.client.post(self.url, route_data, format='json')
        self.assertEquals(response.status_code, 201)

        response = self.client.get(self.url)
        response = response.json()
        self.assertEquals(response['body'].get('count'), 1)

    def test_update(self):
        """test PUT"""
        # test initial order
        route4 = factories.RouteFactory(stations__num=4)
        new_line = factories.LineFactory()
        response = self.client.get(self.url)
        response_dict = response.json()
        self.assertEquals(response_dict['body']['count'], 1)
        self.assertTrue(response_dict['body']['results'][0]['line'].endswith(route4.line.id+'/'))
        self.assertFalse(response_dict['body']['results'][0]['line'].endswith(new_line.id+'/'))
        # get uri to patch
        detail_url = reverse('routemodel-detail', kwargs={'pk': route4.id})
        route4_data = {
            'line': reverse('linemodel-detail', kwargs={'pk': new_line.id}),
            'stations': response_dict['body']['results'][0]['stations'],
        }
        response = self.client.put(detail_url, route4_data, format='json')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(response.json()['line'].endswith(new_line.id+'/'))

    def test_delete(self):
        factories.RouteFactory.create_batch(3)
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        # get which station to delete
        delete_obj = response.json()['body']['results'][0]['url']
        response = self.client.delete(delete_obj)
        self.assertEquals(response.status_code, 204)
        # ensure it was deleted
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['body']['count'], 2)
