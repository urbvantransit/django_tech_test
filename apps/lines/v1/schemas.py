# coding: utf8
from marshmallow import Schema, fields


class LinesSchema(Schema):

    id = fields.String()
    name = fields.String()
    color = fields.Decimal()
