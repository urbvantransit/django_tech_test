# coding: utf-8
from datetime import datetime
from uuid import uuid4

from rest_framework.test import APITestCase, APIClient

from apps.users.factories import (
    AdminPermissionFactory,
    DriverPermissionFactory,
    UserPermissionFactory,
    UserFactory,
    TokenFactory
)


def create_id(identifier):
    id_base = "{}{}{}{}{}{}{}{}"
    now = datetime.utcnow()
    id_base = id_base.format(
        identifier,
        now.year,
        now.month,
        now.day,
        now.hour,
        now.minute,
        now.second,
        str(uuid4())[:8]
    )
    return id_base


class APITestCaseWithClients(APITestCase):
    """User-type based APITestCase."""

    @classmethod
    def setUpTestData(cls):
        """
        This setup configuration has the following components:

        * ``admin_user``
        * ``admin_user_token``
        * ``admin_user_permission``
        * ``auth_admin_client``
        * ``driver_user``
        * ``driver_user_token``
        * ``driver_user_permission``
        * ``auth_driver_client``
        * ``user``
        * ``user_token``
        * ``user_permission``
        * ``auth_client``
        """

        cls.USER_DOES_NOT_HAVE_PERMISSION = 'You do not have permission to '\
            'perform this action.'

        cls.admin_user = UserFactory()
        cls.admin_user_token = TokenFactory(user=cls.admin_user)
        cls.admin_user_permission = AdminPermissionFactory(user=cls.admin_user)

        cls.auth_admin_client = APIClient()
        cls.auth_admin_client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(cls.admin_user_token.key)
        )

        cls.driver_user = UserFactory()
        cls.driver_user_token = TokenFactory(user=cls.driver_user)
        cls.driver_user_permission = DriverPermissionFactory(
            user=cls.driver_user)

        cls.auth_driver_client = APIClient()
        cls.auth_driver_client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(cls.driver_user_token.key)
        )

        cls.user = UserFactory()
        cls.user_token = TokenFactory(user=cls.user)
        cls.user_permission = UserPermissionFactory(user=cls.user)

        cls.auth_client = APIClient()
        cls.auth_client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(cls.user_token.key)
        )
