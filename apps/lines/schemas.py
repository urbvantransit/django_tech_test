# coding: utf8
from marshmallow import (Schema, fields)


class LineSchema(Schema):

    id = fields.String()
    name = fields.String()
    color = fields.String()

class RouteSchema(Schema):

    id = fields.String()
    line = fields.String()
    direction = fields.Boolean()
    is_active = fields.Boolean()