# coding: utf8
from marshmallow import Schema, fields


class LineSchema(Schema):
    id = fields.String()
    name = fields.String()
    color = fields.String()


class RouteSchema(Schema):
    id = fields.String()
    direction = fields.Boolean()
    is_active = fields.Boolean()
    line = fields.Nested(LineSchema)
    # stations = fields.Nested(StationSchema, many=True)

    class Meta:
        fields = ('id', 'line', 'direction', 'is_active')
