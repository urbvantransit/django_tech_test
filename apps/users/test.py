from .factories import (UserFactory, TokenFactory, AdminUserFactory)

class CustomUserTestMixin(object):
    """
        Mixin for user and authorization setup for tests
    """
    username = 'admin'

    def setUp(self):
        """
            Configure the creadentials for the API Client with:
             a real user if a username is configured in the calling class
             otherwise it create a fake user using the UserFactory class
            :return: None
        """
        # TODO: Factories for specific users with specific permissins
        # username =  getattr(self, 'username', None)
        # if username:
        #     self.__real_user_setup(username, 'test_{}'.format(username))
        # else:
        #     self.__fake_user_setup()
        self.__fake_user_setup()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def __real_user_setup(self, username, password):
        self.user = AdminUserFactory()

    def __fake_user_setup(self):
        self.user = UserFactory()
