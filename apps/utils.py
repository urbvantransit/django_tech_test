# coding: utf8
from datetime import datetime
from uuid import uuid4

from django.utils import timezone


def create_id(identifier: str) -> callable:
    """Returns factory function which returns a unique identifier based on `identfier`, the date, and a uuid"""
    def _create_id():
        now = timezone.now()
        uuid_ = str(uuid4())[:8]
        return f'{identifier}{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}{uuid_}'
    return _create_id
