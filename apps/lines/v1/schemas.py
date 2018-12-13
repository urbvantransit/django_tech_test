# coding: utf8
from marshmallow import (Schema, fields)

from apps.stations.v1.schemas import LocationSchema


class LineSchema(Schema):

    id = fields.String()
    name = fields.String()
    color = fields.String()


class RouteSchema(Schema):
    class Meta:
        fields = ('id',
                  'line',
                  #TODO: Add the stations many to many field to the serialization
                  #'stations',
                  'direction',
                  'is_active')

    id = fields.String()
    line = fields.Nested(LineSchema)
    stations = fields.Nested(LocationSchema, many=True, required=False)
    direction = fields.Boolean()
    is_active = fields.Boolean()

