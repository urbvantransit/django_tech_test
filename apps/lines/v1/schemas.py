# coding: utf8
from marshmallow import (Schema, fields)
from apps.stations.v1.schemas import StationSchema


class LineSchema(Schema):

    id = fields.String()
    name = fields.String()
    color = fields.String()


class RouteSchema(Schema):

    id = fields.String()
    direction = fields.Boolean()
    is_active = fields.Boolean()
    line = fields.Nested(LineSchema)
    stations = fields.Method("get_stations")

    def get_stations(self, obj):
        return obj.stations.values()
