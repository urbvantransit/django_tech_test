# coding: utf8
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from users.factories import UserFactory
from . import factories


class LineCRUDTest(APITestCase):
    url = reverse('linemodel-list')

    def setUp(self):
        self.client.force_login(UserFactory())

    def test_list_create(self):
        response = self.client.get(self.url)
        response = response.json()
        self.assertEquals(response['body'].get('count'), 0)

        line_data = dict(name='ruby rod supegreen', color='#8c8832')
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
