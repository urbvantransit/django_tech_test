# coding: utf-8
from datetime import datetime
from uuid import uuid4

from rest_framework.test import APITestCase, APIClient

from apps.users.factories import (UserFactory, TokenFactory)


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

        * ``user``
        * ``user_token``
        * ``client``
        """

        cls.user = UserFactory()
        cls.user_token = TokenFactory(user=cls.user)

        cls.auth_client = APIClient()
        cls.auth_client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(cls.user_token.key)
        )
