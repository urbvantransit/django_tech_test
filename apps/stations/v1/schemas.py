from marshmallow import (Schema, fields)


class LocationSchema(Schema):

    id = fields.String()
    name = fields.String()
    latitude = fields.Decimal()
    longitude = fields.Decimal()


class StationSchema(Schema):
    id = fields.String()
    location = fields.Nested(LocationSchema)
    order = fields.Integer()
    is_active = fields.Boolean()
