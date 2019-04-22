# coding: utf8
from marshmallow import (Schema, fields)

from apps.stations.v1.schemas import StationSchema


class LineSchema(Schema):

    id = fields.String()
    name = fields.String()
    color = fields.String()


class RouteSchema(Schema):
    id = fields.String()
    line = fields.Nested(LineSchema)
    stations = fields.Nested(StationSchema, many=True)
    direction = fields.Boolean()
    is_active = fields.Boolean()
