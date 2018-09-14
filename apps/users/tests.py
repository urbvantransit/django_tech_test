# coding: utf8
from unittest.mock import MagicMock

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import SimpleTestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.viewsets import ModelViewSet

from apps.users.factories import UserFactory, StaffUserFactory
from apps.users.permissions import CustomPermission


class CustomPermissionsTest(SimpleTestCase):
    def setUp(self):
        self.anon_user = AnonymousUser()
        self.user = UserFactory.build()
        self.staff_user = StaffUserFactory.build()
        self.view = ModelViewSet.as_view({
            'get': 'list',
            'post': 'create',
        }, queryset=get_user_model().objects.none(), serializer_class=MagicMock(),
            permission_classes=[CustomPermission])

    def test_anonymous_read(self):
        request = APIRequestFactory().get('/')
        force_authenticate(request, user=self.anon_user)
        response = self.view(request)
        self.assertEquals(response.status_code, 403)

    def test_anonymous_write(self):
        request = APIRequestFactory().post('/', {})
        force_authenticate(request, user=self.anon_user)
        response = self.view(request)
        self.assertEquals(response.status_code, 403)

    def test_authenticated_read(self):
        request = APIRequestFactory().get('/')
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEquals(response.status_code, 200)

    def test_authenticated_write(self):
        request = APIRequestFactory().post('/', {})
        force_authenticate(request, user=self.user)
        response = self.view(request)
        self.assertEquals(response.status_code, 403)

    def test_staff_read(self):
        request = APIRequestFactory().get('/')
        force_authenticate(request, user=self.staff_user)
        response = self.view(request)
        self.assertEquals(response.status_code, 200)

    def test_staff_write(self):
        request = APIRequestFactory().post('/', {})
        force_authenticate(request, user=self.staff_user)
        response = self.view(request)
        self.assertEquals(response.status_code, 201)
