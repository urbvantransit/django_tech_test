# coding: utf8
from marshmallow import (Schema, fields)


class LocationSchema(Schema):

    id = fields.String()
    name = fields.String()
    latitude = fields.Decimal()
    longitude = fields.Decimal()
