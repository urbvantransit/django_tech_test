# coding: utf-8
from marshmallow import Schema
from marshmallow.fields import Bool, Decimal, Nested, String, Integer


class LocationSchema(Schema):

    id = String()
    name = String()
    latitude = Decimal()
    longitude = Decimal()


class StationSchema(Schema):

    id = String()
    location = Nested(LocationSchema)
    order = Integer()
    is_active = Bool()
