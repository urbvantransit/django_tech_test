from enum import Enum

from django.conf import settings
from django.db import models


class UserPermissionModel(models.Model):

    class PERMISSIONS(Enum):
        viewer = ('vw', 'Viewer')
        editor = ('ed', 'Editor')
        owner = ('ow', 'Owner')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        related_name='permissions',
        on_delete=models.CASCADE
    )

    permission = models.CharField(
        max_length=2,
        choices=[permission.value for permission in PERMISSIONS],
        default=PERMISSIONS.get_value('viewer')
    )

    def __str__(self):
        return 'Permission {} of {}'.format(self.permission, self.user)
