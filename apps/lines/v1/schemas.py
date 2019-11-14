# coding: utf8
from marshmallow import (Schema, fields)
from apps.stations.v1.schemas import StationSchema


class LinesSchema(Schema):

    id = fields.String()
    name = fields.String()
    color = fields.Decimal()


class RouteSchema(Schema):

    id = fields.String()
    line = fields.String()
    stations = fields.Nested(StationSchema, many=True, required=False)
    direction = fields.Boolean()
    is_active = fields.Boolean()
