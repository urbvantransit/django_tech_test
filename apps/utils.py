# coding: utf8
from datetime import datetime
from uuid import uuid4


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


def create_location_id():
    return create_id('location_')


def create_station_id():
    return create_id('station_')


def create_line_id():
    return create_id('line_')


def create_route_id():
    return create_id('route_')
